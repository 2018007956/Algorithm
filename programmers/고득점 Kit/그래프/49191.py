# Not Solved
def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]
    for a,b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j or board[i][j] in [1, -1]:
                    continue
                
                if board[i][k]==board[k][j]==1:
                    board[i][j]=1
                    board[j][i]=board[k][i]=board[j][k]=-1
        
    for row in board:
        if row.count(0)==1:
            answer += 1
    return answer
'''
처음엔 '순위를 매길 수 있다'는 의미는 그래프 관점에서, 모든 사람과 연결되어 있다는 뜻으로 해석했고, 
그 사람과 간선 하나로 연결된 경우를 모두 카운트하는 식으로 알고리즘을 구현했음
=> 반례) 모두 연결되어 있어도 사이클이 발생하면 순위 알 수 없음

플로이드와샬 알고리즘 사용
a가 c를 이기고 c가 b를 이기는 관계가 있으면,
a가 b를 이긴 것으로 체크하고 (b,a), (c,a), (b,c)는 모두 진 것으로 체크
=> 순위가 결정되려면, 체크된 값의 개수가 n-1(=체크되지 않은 값이 1)이면 됨
'''

# 다른 사람 풀이
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        win[result[0]].add(result[1])
        lose[result[1]].add(result[0])

    # 간접 승패 관계 확장
    # A->B->C이면 A->C 관계 추가
    for i in range(1, n + 1):
        # i를 이긴 선수들은, i가 이긴 사람도 이긴 셈
        for winner in lose[i]: 
            win[winner].update(win[i])
        # i에게 진 선수들은, i가 진 사람에게도 진 셈
        for loser in win[i]: 
            lose[loser].update(lose[i]) 

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: 
            answer += 1
    return answer