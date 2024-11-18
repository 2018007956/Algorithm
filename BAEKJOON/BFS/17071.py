# 풀이 공부
from collections import deque
def bfs(N, K):
    if N==K:
        print(0)
        return
    
    queue = deque([N])
    visited[0][N] = True
    time = 0
    while queue:
        time += 1
        K += time
        if K > 500000:
            break

        for _ in range(len(queue)):
            X = queue.popleft()
            for nx in [X-1, X+1, 2*X]:
                if 0 <= nx <= 500000 and not visited[time%2][nx]:
                    visited[time%2][nx] = True
                    queue.append(nx)

        if visited[time%2][K]:
            print(time)
            return
    
    print(-1)    

N, K = map(int, input().split())
visited = [[False] * 500001 for _ in range(2)]
bfs(N, K)