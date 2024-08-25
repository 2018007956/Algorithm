# Solved (45m)
import sys
input = sys.stdin.readline

def dfs(img): # img: 2-D array
    n = len(img)
    flatten = [img[i][j] for j in range(n) for i in range(n)]
    if all(flatten): # 모두 1이면
        print('1', end='')
    elif not any(flatten): # 모두 0이면
        print('0', end='')
    else: 
        # 1과 0이 섞인 경우 4분할
        print('(', end='')
        dfs([[img[i][j] for j in range(n//2)] for i in range(n//2)]) # 왼쪽 위
        dfs([[img[i][j] for j in range(n//2, n)] for i in range(n//2)]) # 오른쪽 위
        dfs([[img[i][j] for j in range(n//2)] for i in range(n//2, n)]) # 왼쪽 아래
        dfs([[img[i][j] for j in range(n//2, n)] for i in range(n//2, n)]) # 오른쪽 아래
        print(')', end='')


N = int(input())
img = [input() for _ in range(N)]
dfs([[int(img[i][j]) for j in range(N)] for i in range(N)])