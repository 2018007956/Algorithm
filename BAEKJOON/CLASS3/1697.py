# Solved (53m)
from collections import deque
def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x]-1)
            break
        for i in [x*2,x+1,x-1]:
            if 0 <= i <= 100000 and not visited[i]: 
                queue.append(i)   
                visited[i] = visited[x] + 1
            
N, K = map(int, input().split())
visited = [False] * (100001)
bfs(N)

'''
8:57~24 (27m) 푸는중
여러가지 이동 수 존재 -> 너비우선탐색 알고리즘 사용
Ref: 5014번 스타트링크 문제와 유사

9:05~14 (9m) 런타임에러
    visited 범위 수정 (+1)
    
N=0일 때 출력값이 항상 1 높게 나옴
젤 처음 visited[N]을 0으로 주면 두번 방문 발생하므로 1로 시작하고, 마지막 출력에서 -1 해줌

~31 (17m) Solved
'''