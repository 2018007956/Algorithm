# Solved (2h)
import sys
input = sys.stdin.readline

def check_able(x, y):
    able_num = [1,2,3,4,5,6,7,8,9]
    
    for i in range(9):
        if board[y][i] in able_num:
            able_num.remove(board[y][i])
        if board[i][x] in able_num:
            able_num.remove(board[i][x])

    # x,y가 속한 3x3 사각형의 시작 위치
    start_x = (x//3)*3
    start_y = (y//3)*3
    for i in range(3):
        for j in range(3):
            if board[start_y+i][start_x+j] in able_num:
                able_num.remove(board[start_y+i][start_x+j])
    
    return able_num

def dfs(depth):
    if depth==len(zero_pos):
        for row in board:
            print(*row)
        exit()

    x, y = zero_pos[depth]
    able_num = check_able(x, y)
    for num in able_num:
        board[y][x] = num
        dfs(depth+1)
        board[y][x] = 0


board = [list(map(int, input().split())) for _ in range(9)]
zero_pos = []
for x in range(9):
    for y in range(9):
        if board[y][x]==0:
            zero_pos.append((x, y))

dfs(0)
'''
3x3 체크하는 법 서치함

이후 다른 값에 의해 기존의 값이 back할 수 도 있어서 dfs 종료 조건을 return으로 했었는데, 
생각해보니 1~9까지 매번 탐색하며 세 조건을 따지기 때문에 if depth==zero_num을 만난 순간이 정답임
exit() 사용

12:02~14, 4:34~5:11 (49m) python, pypy 모두 72% 시간초과
    dfs 탐색 횟수를 줄이기 위해, num을 1~9까지 매번 탐색하는게 아니라 탐색 가능하지 않은 숫자는 미리 제거 후 탐색
    ref) https://dd-developer.tistory.com/57

    수정 전 코드
    for num in range(1, 10):
        if num not in board[y] and num not in list(zip(*board))[x] and check_rect(x, y, num):
        
    수정 후 코드
    for num in check_able(x, y):
    
~43 (32m) pypy 72% 시간초과
    행과 열을 동시에 탐색하는 구조로 수정
    이 부분은 시간복잡도 개선에 영향을 안끼칠 것 같은데, Solved 된 이유를 모르겠음

~6:23 (40m) pypy Solved
'''