from collections import deque
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dir_ = [1, 2, 4, 8]
def bfs(y, x, room_id):
    global room_cnt, room_max
    queue = deque([(y, x)])
    visited[y][x] = True
    room_id_board[y][x] = room_id
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for i, (dx, dy) in enumerate(move):
            nx = x + dx
            ny = y + dy
            if 0<=ny<M and 0<=nx<N and not visited[ny][nx] and board[y][x]&dir_[i]!=dir_[i]:
                visited[ny][nx] = True
                room_id_board[ny][nx] = room_id
                queue.append((ny, nx))
                cnt += 1
    
    room_cnt += 1
    # room_max = max(room_max, cnt)
    room_sizes[room_id] = cnt


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
room_id = 0
room_sizes = dict()
room_id_board = [[-1]*N for _ in range(M)]
room_cnt = 0
# room_max = 0
room_del = 0
for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            bfs(y, x, room_id)
            room_id += 1

# 벽 하나 제거 시 최대 크기 찾기
max_combined = 0
for y in range(M):
    for x in range(N):
        for i, (dx, dy) in enumerate(move):
            nx = x + dx
            ny = y + dy
            if 0<=ny<M and 0<=nx<N:
                id1 = room_id_board[y][x]
                id2 = room_id_board[ny][nx]
                if id1!= id2:
                    combined = room_sizes[id1] + room_sizes[id2]
                    max_combined = max(max_combined, combined)

print(room_cnt)
print(max(room_sizes.values()))
print(max_combined)
'''
[3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기]를 어떻게 구해야할지 모르겠어
IDEA>
1. 각 방마다 번호를 매기고 크기를 저장한다.
2. 그 다음, 모든 좌표를 순회하면서 인접한 방이 다른 방일 때, 그 사이의 벽을 "가상의 제거" 했을 때의 크기를 계산한다.
3. 가장 큰 값을 업데이트 해주면 끝!
새로운 변수 선언 : room_id_board - 각 좌표별 방번호 저장, room_sizes - 방 번호별 방의 넓이 저장
'''