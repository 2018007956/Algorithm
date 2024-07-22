# Solved (58m)
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
tmp = list(map(int, input().split()))
knower = []
if tmp[0] != 0:
    num_of_know, knower = tmp[0], tmp[1:]
    
party = [[] for _ in range(M)]
for i in range(M):
    tmp = list(map(int, input().split()))
    if tmp[0] != 0:
        num_of_participate, participater = tmp[0], tmp[1:]
        party[i].extend(participater)

# find connection
def bfs(start):
    queue = deque(start)
    for x in start:
        know_truth[x] = True
    
    while queue:
        x = queue.popleft()
        for people in party:
            if x in people:
                for adj in people:
                    if not know_truth[adj]:
                        queue.append(adj)
                        know_truth[adj] = True

know_truth = [False] * (N+1)
bfs(knower)

# count the number of parties that can be exaggerated
exaggerate = 0
for idx, people in enumerate(party):
    for person in people:
        if know_truth[person]:
            break
    else:
        exaggerate += 1

print(exaggerate)
'''
되도록 과장, 거짓말쟁이는 X
과장된 이야기를 할 수 있는 파티 개수의 최대 수 구하기
조건
1. 진실을 아는 사람이 있을 땐 거짓말 못함
2. 한 사람은 이야기를 일관되게 들어야 함

내 풀이> 
지민이가 파티를 참석하면서 진실을 알 수 있는 사람들을 knower에 넣음
파티를 한번 더 돌면서 과장 할 수 있는 파티 수 세기
-> 너무 단순하게(직관적으로) 풀어서 시간 초과 걸릴 것 같은데 주어진 범위가 작다. 간과한 부분이 있나?

1:55~30 (35m) 1%? 틀렸습니다
반례 : https://www.acmicpc.net/board/view/111041
5 4
1 5
2 1 2
2 2 3
2 3 4
2 4 5
[정답] 0 
[출력] 2
<마지막에 knower에 추가되면 앞 파티에서 knower이지만 추가되지 않는 사람 발생. 반영이 연쇄적으로 되지않음>
=> 연결된 사람을 표현하기 위해 bfs로 추적

~42, 3:05~16 (23m) Solved
'''