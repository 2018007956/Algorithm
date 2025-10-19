from api import *

URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
USER_NUM = 30

if __name__ == "__main__":
    auth_key = start_api(URL, 1)

    pairs = []
    cmd = []
    for i in range(1, USER_NUM + 1):
        cmd.append({"id": i, "grade": 5000}) # 초기 등급값 임의 설정
    change_grade_api(URL, auth_key, cmd)

    result = 'ready'

    while result == 'ready':
        response = match_api(URL, auth_key, pairs)
        result = response['status']
        time = response['time']
        max_time = 0
        waiting_lines = waiting_line_api(URL, auth_key)

        user_grade = [0] * (USER_NUM + 1)
        for user_info in user_info_api(URL, auth_key): # 매 시간마다 최신 등급 기준으로 매칭
            user_grade[user_info['id']] = user_info['grade']

        for waiting_line in waiting_lines: # 각 유저 대기시간 중 최대값 갱신
            max_time = max(time - waiting_line['from'], max_time)

        # 매칭 로직, 파라미터는 임의 지정
        if time <= 540:
            pairs = match_users(user_grade, waiting_lines, 3, max_time, 4) # 안정적인 매칭
        elif time < 555:
            pairs = match_users(user_grade, waiting_lines, 2, max_time, 4) # 후반부라 실력 비슷한 상대 빠르게 잡음
        elif time == 555:
            pairs = match_users(user_grade, waiting_lines, 0, max_time, 14) # 막판이라 대기자 남기지 않기 위해 강제 매칭
        elif time <= 595: # 매칭 중단
            pass
            
        for game_result in game_result_api(URL, auth_key):
            winner = game_result['win']
            loser = game_result['lose']
            taken = game_result['taken']

            # 시간 가중치 + 점수 가중치 (높은 점수의 상대를 이기면 더 높은 점수를 부여)
            point = ((40 - taken) + 1) * 10

            user_grade[winner] += point + (user_grade[loser] // 100)
            user_grade[loser] -= point + (100 - (user_grade[winner] // 100))

        cmd = []
        for i in range(1, USER_NUM + 1):
            cmd.append({"id": i, "grade": user_grade[i]})
        change_grade_api(URL, auth_key, cmd)

    score_api(URL, auth_key)
