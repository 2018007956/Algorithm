# Solved (1h 13m)
import sys
from collections import deque
input = sys.stdin.readline

node = int(input())
edge = int(input())
graph = [[] for _ in range(node+1)]
for _ in range(edge):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
visited = [False] * (node+1)
visited[1] = True
queue = deque(graph[1])

while queue:
    i = queue.popleft()
    visited[i] = True
    for x in graph[i]:
        if not visited[x]:
            queue.append(x)
            
print(sum(visited)-1)

'''
8:54~9:12 (18m) 시간초과
1<=node<=100, 제한 시간 1초
=> pop(0)이 O(n)라서 최악의 경우 100(node)*100(pop)*100(add)=1,000,000?
=> 중복된 노드를 여러 번 방문하는 경우 있기 때문에 pop되는 node수가 최대 100이라 가정할 수 없음
=> deque popleft로 수정하고, 중복된 노드 방문을 하지 않기 위해 visited 배열 생성 "bfs"

9:12~9:34 (22m) 틀렸습니다
=> graph 단방향 -> 양방향으로 수정
=> visited = True 선언 위치 수정
반례
2
1
2 1
[정답] 1
[출력] 0
연결된 노드들을 돌면서 visited 하는게 아니라 pop 했을때 그 위치에 대해 visited=True해줘야 됨

9:34~10:07 (33m) Solved
'''