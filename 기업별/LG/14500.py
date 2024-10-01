# Solved (1h 20m) w/ Search
# Point) ㅗ 모양 고려 & 백트래킹 가지치기
import sys
input = sys.stdin.readline

move = [(1,0), (-1,0), (0,1), (0,-1)]
def dfs(depth, y, x):
    global max_val, sum_val

    # 백트래킹 최적화를 위한 조건 : 남은 칸들을 모두 최대값이라고 가정해도 현재 값보다 작다면 가지치기
    if max_val >= sum_val + max_val * (4-depth):
        return
    
    if depth == 4:
        max_val = max(max_val, sum_val)
        return
    
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
            if depth == 2:
                visited[ny][nx] = True
                sum_val += arr[ny][nx]
                dfs(depth+1, y, x)
                visited[ny][nx] = False
                sum_val -= arr[ny][nx]
            visited[ny][nx] = True            
            sum_val += arr[ny][nx]
            dfs(depth+1, ny, nx)
            visited[ny][nx] = False
            sum_val -= arr[ny][nx]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_val = 0
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        sum_val = arr[i][j]
        dfs(1, i, j)
        visited[i][j] = False
        sum_val = 0

print(max_val)
'''
10:49~11:48 (1h) 
예제 3이 답 6이 나와서 보니까 ㅗ 모양이 고려안된듯
    백트래킹으로 해야 될 것 같아 // 백트래킹으로 해도 똑같음 // ㅗ, ㅓ 형태 고려 어떻게??

풀이 참고
    depth==2일 때 (즉, 두 개의 블럭을 선택했을 때) 새로운 블럭에서 다음 블럭을 탐색하는게 아니라
    다시 기존블럭에서 탐색하게 만들면 ㅗ모양 만들 수 있음

~32 (10m) 1% 시간초과
    가지치기 조건 추가

~40 (8m)Solved
'''