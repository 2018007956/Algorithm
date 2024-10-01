# Solved (40m)
import sys
from collections import deque
input = sys.stdin.readline

move = [(1,0), (-1,0), (0,-1), (0,1)]
def bfs(y, x):
    start_val = A[y][x]
    visited[y][x] = 1
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=ny<N and 0<=nx<M and A[ny][nx]!=0 and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))

    last_val = A[y][x]
    result.append((visited[y][x], start_val + last_val)) 


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = []
for i in range(N):
    for j in range(M):
        if A[i][j]!=0:
            visited = [[False] * M for _ in range(N)]
            bfs(i, j)

if result:
    result.sort(reverse=True)
    print(result[0][1])
else:
    print(0)
    
'''
11:14~53 (40m) 
문제는 20분도 안걸려서 어느정도 구현했는데,
그리드에서 끝과 끝을 어떻게 찾지? 라는 고민을 하다가 20분을 보냄
=> 가장 긴 라인을 출력해야 하기 때문에, 끝과 끝을 찾을 필요 없이 라인의 길이만을 저장하고 정렬해서 찾으면 됨

시작 방과 끝 방은 동일한 위치일 수 있음
    => 이 조건은 사이클이 발생하면 그 중 젤 큰 숫자 *2
    => 라고 생각했는데 예제2를 보면 정답 8이 아니라 5임
    계속 '가장 긴 라인을 출력한다'는 조건을 간과하고 있었음
    따라서 이 조건은 한 칸이 독립적으로 값을 가진 경우를 말하는 거고
    위의 코드로 고려됨
'''