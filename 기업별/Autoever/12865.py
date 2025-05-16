import sys
input = sys.stdin.readline
N, K = map(int, input().split())
value_board = [[0] * (K+1) for _ in range(N+1)]
for n in range(1, N+1):
    w, v = map(int, input().split())
    for k in range(1, K+1):
        if k < w:
            value_board[n][k] = value_board[n-1][k]
        else:
            value_board[n][k] = max(value_board[n-1][k-w]+v, value_board[n-1][k])

print(value_board[n][k])
# for i in range(n):
#     print(value_board[i])