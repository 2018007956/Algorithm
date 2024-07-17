# Solved (28m)
from collections import deque
def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x]-1)
            break

        if 0 <= x*2 <= 100000 and (not visited[x*2] or visited[x] < visited[x*2]):
            queue.append(x*2)
            visited[x*2] = visited[x]

        for i in [x+1,x-1]:
            if 0 <= i <= 100000 and (not visited[i] or visited[x]+1 < visited[i]): 
                queue.append(i)   
                visited[i] = visited[x] + 1
        
N, K = map(int, input().split())
visited = [False] * (100001)
bfs(N)
'''
7% (8m) 틀렸습니다
    큐에 쌓아서 bfs를 수행할 때에는 우선순위를 잘 고려해야 한다
    이 문제에서는 시간(초)에 따른 우선순위를 고려하여, 같은 시간상에서 탐색을 모두 마치도록 수행해야 한다.

~29 (8m) 40% 쯤 틀렸습니다
    간선의 길이가 다양한 그래프에서 BFS를 하고 있기 때문에 처음 찾은 경로가 최단이 아닐 수 있습니다. 
    그래서 갱신 조건을 “-1이 아니면“이 아니라 ”역대 최단거리보다 가까우면“으로 걸어야 합니다.

~41 (12m) Solved
'''