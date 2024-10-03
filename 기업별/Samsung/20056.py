# Solved (1h 25m) w/ Search
from collections import deque
N, M, K = map(int, input().split())
fireball = deque([])
for r, c, m, d, s in [list(map(int, input().split())) for _ in range(M)]:
    r, c = r-1, c-1
    fireball.append((r, c, m, d, s))

board = [[[] for _ in range(N)] for _ in range(N)] 
move = [(-1,0), (-1,1),(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

for _ in range(K):
    # 1. 모든 파이어볼이 자신의 방향 d로 속력 s칸만큼 이동한다.
    while fireball:
        r, c, m, s, d = fireball.popleft()
        nr = (r + move[d][0] * s) % N
        nc = (c + move[d][1] * s) % N
        board[nr][nc].append([m, s, d])

    # 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                nm = sum([x[0] for x in board[i][j]])//5
                if nm > 0:
                    ns = sum([x[1] for x in board[i][j]])//len(board[i][j])
                    if all([x[2]%2==0 for x in board[i][j]]) or all([x[2]%2==1 for x in board[i][j]]):
                        for nd in range(0, 7, 2):
                            fireball.append([i, j, nm, ns, nd])
                    else:
                        for nd in range(1, 8, 2):
                            fireball.append([i, j, nm, ns, nd])
                board[i][j] = []
            
            if len(board[i][j]) == 1:
                fireball.append([i, j] + board[i][j].pop())
    
print(sum([f[2] for f in fireball]))