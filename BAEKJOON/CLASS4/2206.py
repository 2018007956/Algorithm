# 풀이 공부
import sys
from collections import deque
input = sys.stdin.readline
move = [(0,1), (0,-1), (-1,0), (1,0)]
def bfs(x, y):
    queue = deque([(x, y, 0)]) # x좌표, y좌표, 부순 횟수
    visited[y][x][0] = 1
    while queue:
        x, y, break_cnt = queue.popleft()
        if (x,y) == (M-1,N-1):
            return visited[y][x][break_cnt]
        
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=ny<N and 0<=nx<M:
                # 벽인 경우 벽 부수기
                if jido[ny][nx]=='1' and break_cnt==0:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    queue.append((nx, ny, 1))

                # 이동 가능하며, 해당 break_cnt 층에서 아직 방문하지 않은 경우
                if jido[ny][nx]=='0' and visited[ny][nx][break_cnt]==0:
                    visited[ny][nx][break_cnt] = visited[y][x][break_cnt] + 1
                    queue.append((nx, ny, break_cnt))
    
    return -1

N, M = map(int, input().split())
jido = [input() for _ in range(N)]
# 3차원 배열 index 0 : 벽을 안 부수고 가는 경로 / index 1 : 벽을 부수고 가는 경로
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
print(bfs(0, 0))

# for c in visited:
#     print(*c)

'''
- 지도의 숫자를 str로 받고 조건은 int로 넣어줘놓고 왜 조건이 안먹지 고민하고 있었음. 타입 매치 신경쓰기

길이 막혔을 때 벽을 한번 부수도록 구현했는데,
만약 길이 막히지 않고 (N,M)에 도달 가능한데, 벽을 한번 부쉈을 떄 더 거리가 짧아질 수 있는 경우를 고려해줘야 함
[입력]
6 4
0000
1110
1000
0000
0111
0000
[출력]
9

- 최소 거리를 갱신하고 있기 때문에 visited[ny][nx]>=visited[y][x]+1 탐색 조건 필요 

(내 코드)
import sys
from collections import deque
input = sys.stdin.readline
move = [(0,1), (0,-1), (-1,0), (1,0)]
break_wall = False
min_dist = 1e8
def bfs(jido, x, y):
    global break_wall, min_dist
    queue = deque([(x, y)])
    visited[y][x] = 1
    while queue:
        x, y = queue.popleft()
        can_go = False
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=ny<N and 0<=nx<M and (not visited[ny][nx] or visited[ny][nx]>=visited[y][x]+1):
                if jido[ny][nx]=='0':
                    can_go = True # 갈 수 있는 길이 있다고 체크
                    queue.append((nx, ny))
                    visited[ny][nx] = visited[y][x] + 1
        
        # finish
        if y==N-1 and x==M-1:
            min_dist = min(min_dist, visited[N-1][M-1])
            return
        
        # 상하좌우 탐색 후 길이 막혔을때, 벽 부수기 체크
        if not can_go and not break_wall: 
            break_wall = True
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if 0<=ny<N and 0<=nx<M and jido[ny][nx]=='1':
                    queue.append((nx, ny))
                    visited[ny][nx] = visited[y][x] + 1

        
    if break_wall: # 벽을 한번 부숴도 도달 불가능
        min_dist = -1

N, M = map(int, input().split())
jido = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
bfs(jido, 0, 0)

# 만약 벽부숨 없이 (N,M)까지 도달 가능하다면, 
# 임의의 벽을 하나 없애서 최단 경로 찾아보기
if not break_wall:
    wall_position = [(i,j) for j in range(M) for i in range(N) if jido[i][j]=='1']
    for i, j in wall_position:
        copy_jido = [item[:] for item in jido]
        copy_jido[i] = list(copy_jido[i])
        copy_jido[i][j] = '0'
        copy_jido[i] = ''.join(copy_jido[i])
        visited = [[False] * M for _ in range(N)]
        bfs(copy_jido, 0, 0)

print(min_dist)

11:03~12:57 (1h 54m) 2% 메모리초과
    copy_jido 때문인가? 했는데 gpt한테 물어보니
    주요 원인은 visited 배열의 관리와 벽을 부순 상태를 고려한 bfs탐색 방식 때문일 수 있다고 했다.
    내 코드에서는 벽을 부수지 않았을 때와 부수었을 때를 구분하지 않고 방문 여부를 체크하기 때문에 메모리와 시간이 더 많이 소요될 수 있다.

개선 방안
1. visited 배열 개선: 벽을 부수지 않은 상태와 부순 상태를 따로 체크하도록 visited 배열을 3차원으로 사용
    visited[y][x][0]은 벽을 부수지 않고 방문했을 때의 상태, visited[y][x][1]은 벽을 부수고 방문했을 때의 상태를 나타냄
2. 벽의 위치 저장 없이 즉시 처리: wall_position 배열을 사용하지 않고 벽을 부술 수 있는 경우를 즉시 처리
    BFS를 실행할 때 벽을 만난 경우 벽을 부수고 이동할 수 있는지 확인하고 진행
3. 메모리 사용 최적화: 2차원 배열이나 리스트 복사 대신 상태를 간단히 표시할 수 있는 방식으로 접근
Ref) https://great-park.tistory.com/110

* 한 벽을 부수는 경우의 수를 모두 각각 bfs 돌려서 최소 거리를 계산하는 게 아니라
벽을 부수는 경우와 부수지 않는 경우를 동시에 탐색해나감
'''