# Not Solved
# 알고리즘 : 그리디
# 현 시각 떠 있는 서버 수를 계산하고, 부족하면 그만큼만 추가
def solution(players, m, k):
    history = [] # 증설 횟수
    
    for player in players:
        total = sum((history + [1])[-k:]) * m # 가능한 최대 인원 수
        if total > player:
            history = history + [0]
        else: # 서버 증설
            add = (player - total) // m + 1
            history += [add]
    
    return sum(history)
# 이용자가 m명 미만이면 증설 불필요(= 기본 1대가 m명을 처리)
# => 기본 서버 1대가 항상 가동된다고 전제
# Line 7 : + [1]을 빼면 첫 시각에 players[0] == 0이어도 “현재 용량(total)=0, player=0 → 부족하다고 보고 1대 증설” 같은 오동작이 발생


# 다른 풀이
import heapq as hq
def solution(players, m, k):
    answer = 0
    pq = []
    
    server = 1
    for time in range(24):
        player = players[time]
        while pq and pq[0] <= time:
            server -= 1
            hq.heappop(pq)
            
        remain = player - server * m
        if remain < 0:
            continue
            
        while remain >= 0:
            answer += 1
            server += 1
            hq.heappush(pq, time + k)
            remain -= m
            
    return answer
'''
Greedy Algorithm
1. 현재 시간에 반납해야 하는 서버가 존재하는지 확인한다.
    PriorityQueue에 '증설된 서버의 종료 시각'을 저장했다.
    증설된 서버의 운영 시간이 고정적이기 때문에 다른 방법을 사용할 수 있을것 이라고 생각한다.
2. 남은 서버로 현재 이용자를 감당할 수 없다면 증설한다.
    서버 하나 늘리는 방식을 사용했다.
    나누기 연산과 나머지 연산을 사용해 한번에 할 수 있었지만 직관적으로 while문으로 작성하였다.
    while remain >= 0 : 부분을 아래와 같이 작성가능

    need = remain//m + 1
        answer += need
        server += need
        
        for _ in range(need): # t시각에 서버를 need대 증설
            hq.heappush(pq, time + k)
            
    return answer
'''