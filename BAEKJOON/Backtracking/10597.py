# Solved (1h) w/ Search
def dfs(i, result):
    if i==len(kriii):
        print(*result)
        exit()
    
    # 한 자리 숫자 처리
    if i < len(kriii):
        num = int(kriii[i])    
        if not visited[num]:
            visited[num] = True
            dfs(i+1, result+[num])
            visited[num] = False

    #  두 자리 숫자 처리
    if i+1 < len(kriii):
        num = int(kriii[i:i+2])
        if num <= N and not visited[num]:
            visited[num] = True
            dfs(i+2, result+[num])
            visited[num] = False
    

kriii = input()
N = len(kriii) if len(kriii) < 10 else 9 + (len(kriii) - 9) // 2
visited = [False] * (N+1)
dfs(0, [])
'''
11:00~12 (12m) 런타임 에러 (IndexError)
    not visited 제대로 구현
    exit() 사용

~ 43 (31m) 90% 틀렸습니다
    1부터 N까지의 수로 이루어져있는데, 최대 50개의 수라고 해서 N은 50인줄 알았다.
    N은 50 이하의 숫자이지만, 입력된 문자열에서 등장하는 숫자의 개수를 결정하는 것이 핵심
    ***N의 정의***
    입력 문자열의 길이에 따라 한 자리 숫자와 두 자리 숫자가 어떻게 배분되는지를 고려하여 N 값을 계산
    Ref) https://dogsavestheworld.tistory.com/entry/python-%EB%B0%B1%EC%A4%80-10597%EB%B2%88-%EC%88%9C%EC%97%B4-%EC%9E%A5%EB%82%9Cbacktracking

    예를 들어 "123456"은 1부터 6까지의 숫자를 나타내지만, N을 50으로 고정하면 불필요하게 두 자리 숫자들까지 고려하게 되어 잘못된 탐색이 이루어짐
    입력 문자열의 길이에 따라 N을 적절히 조정해주지 않으면, 문제에서 요구하는 대로 "1부터 N까지"의 숫자를 올바르게 추출할 수 없다
    
~12:00 (17m) Solved
'''