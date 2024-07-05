# Solved (2h 7m)
R, C = map(int, input().split())
board = [input() for _ in range(R)]
move = [(0,1), (0,-1), (-1,0), (1,0)]

# stack = set()
# stack.add(board[0][0])
def dfs(x, y, cnt):
    global max_visited
    max_visited = max(max_visited, cnt)
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0<=nx<R and 0<=ny<C and not visited[ord(board[nx][ny])-65]:#board[nx][ny] not in stack:
            # stack.add(board[nx][ny])
            visited[ord(board[nx][ny])-65] = True
            dfs(nx,ny, cnt + 1)
            # stack.remove(board[nx][ny])
            visited[ord(board[nx][ny])-65] = False

max_visited = 0
visited = [0] * 26
visited[ord(board[0][0])-65] = True
dfs(0,0,1)
print(max_visited)
'''
8:43~10:08 1% 시간 초과
    리스트를 딕셔너리로 변환 
~22 시간 초과, PyPY3 제출은 그래도 퍼센트 좀 올라가다가 시간 초과
    스택 대신 비트마스크 사용
~32 1% 시간 초과, PyPy3 7% 시간 초과
    인터넷 참고, len(stack)으로 max값 업데이트 대신 cnt 파라미터 추가 => 1% 시간 초과, PyPy 14% 시간 초과
    list를 set으로 변경 => PyPy3 
    아스키 코드 개념 사용하여 방문 문자 확인
~50 1% 시간초과, PyPy Solved!!
'''