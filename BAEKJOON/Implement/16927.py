# Solved (45m)
import sys
from collections import deque
input = sys.stdin.readline
N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * M for _ in range(N)]
deq = deque()
for i in range(min(N, M)//2):
    deq.extend(A[i][i:M-i]) # 위
    deq.extend([x[M-i-1] for x in A[i+1:N-i-1]]) # 오른쪽
    deq.extend(A[N-i-1][i:M-i][::-1]) # 아래
    deq.extend([x[i] for x in A[i+1:N-i-1]][::-1]) # 왼

    deq.rotate(-R)

    for j in range(i, M-i): # 위
        result[i][j] = deq.popleft()
    for j in range(i+1, N-i-1): # 오른쪽
        result[j][M-i-1] = deq.popleft()
    for j in range(M-i-1, i-1, -1): # 아래
        result[N-i-1][j] = deq.popleft()
    for j in range(N-i-2, i, -1): # 왼
        result[j][i] = deq.popleft()


for line in result:
    print(*line)

'''
오른쪽 왼쪽 넣을때 list(map(list, zip(*A[i+1:N-i-1])))[M-i-1] 이렇게 구현하면 빈 리스트인 경우 IndexError 발생하므로
[x[M-i-1] for x in A[i+1:N-i-1]] 이렇게 접근하며 넣어줘야함
'''