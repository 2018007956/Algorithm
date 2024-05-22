import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    visited = [False] * (10001)
    
    queue = deque([[a, '']])
    visited[a] = True
    while queue:
        n, cmd = queue.popleft()
        if n==b:
            print(cmd)
            break

        nx = 2*n % 10000
        if not visited[nx]:
            queue.append([nx, cmd+'D'])
            visited[nx] = True

        nx = (n-1) % 10000
        if not visited[nx]:
            queue.append([nx, cmd+'S'])
            visited[nx] = True
        
        nx = n//1000 + (n%1000)*10
        if not visited[nx]:
            queue.append([nx, cmd+'L'])
            visited[nx] = True

        nx = (n%10)*1000 + n//10
        if not visited[nx]:
            queue.append([nx, cmd+'R'])
            visited[nx] = True

'''
8:55~9:33 () 런타임에러
    문제 조건 잘못 반영한게 있었음 (n-1==0이라면이 아니라 n==0이라면)

~37 (4m) 3% 시간초과
    n==0 으로 조건문 분기 하지 않고 (n-1)%10000 사용
    rotate를 문자열 slicing 으로 구현하는 대신 수식으로 구현

~50 (13m) python3 제출은 그대로 3% 시간초과, pypy3로 제출하여 Solved
    python3 통과 코드들 확인해보니 역방향 BFS도 탐색해줌
'''