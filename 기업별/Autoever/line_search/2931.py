import sys
from collections import deque
input = sys.stdin.readline
dir_ = [(-1,0), (0,-1), (0,1), (1,0)]
move = {
    '|':[(0,-1), (0,1)], 
    '-':[(-1,0), (1,0)], 
    '+':[(-1,0), (0,-1), (0,1), (1,0)], 
    '1':[(0,1), (1,0)], 
    '2':[(0,-1), (1,0)], 
    '3':[(-1,0), (0,-1)],
    '4':[(-1,0), (0,1)]
}
find_pipe = []
def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    chk = False # 삭제된 블록 이후 이어 탐색하기 위함
    find_pipe = False
    while queue:
        x, y = queue.popleft()
        if board[y][x]=='Z' and find_pipe==True:
            break
        
        if board[y][x]=='M' or chk==True or (board[y][x]=='Z' and find_pipe==False):
            chk = False
            for dx, dy in dir_:
                nx = x + dx
                ny = y + dy
                if 0<=ny<r and 0<=nx<c and board[ny][nx]!='.' and not visited[ny][nx]:
                    queue.append((nx, ny))
                    visited[ny][nx] = True  

        else: # 파이프
            if board[y][x]=='.':
                print(y+1, x+1, end=' ')
                chk = True

                # 좌우양옆 확인해서 없어진 파이프 모양 찾기
                ### 좌우양옆 존재 유무가 아니라 모양을 고려해줘야 함
                ### 현재 이동 방향의 반대방향의 좌표가 해당 파이프 모양의 이동방향에 존재하는지 확인
                temp = []
                for dx, dy in dir_:
                    nx = x + dx
                    ny = y + dy
                    if 0<=ny<r and 0<=nx<c and board[ny][nx] not in ('.','M', 'Z'):
                        if (-dx, -dy) in move[board[ny][nx]]:
                            temp.append((dx, dy))
                
                for key, val in move.items():
                    if val==temp:
                        print(key)
                        find_pipe = True

            else:
                for dx, dy in move[board[y][x]]:
                    nx = x + dx
                    ny = y + dy
                    if 0<=ny<r and 0<=nx<c and not visited[ny][nx]:
                        queue.append((nx, ny))
                        visited[ny][nx] = True


r, c = map(int, input().split())
board = [input() for _ in range(r)]
visited = [[False] * c for _ in range(r)]
start_pos = [(x, y) for y in range(r) for x in range(c) if board[y][x]=='M']
bfs(start_pos[0][0], start_pos[0][1])
'''
46%쯤 틀렸습니다
반례? https://www.acmicpc.net/board/view/157929
>> '.'보다 'Z'에 먼저 도착할 수 있는 경우 간과

71%쯤 런타임에러 (KeyError)
    해결 : move 접근할 때 다른 문자 들어갈 수 있는 부분 찾아서 수정
'''