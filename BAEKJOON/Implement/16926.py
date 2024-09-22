# 풀이 공부
import sys
from collections import deque
input = sys.stdin.readline
N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * M for _ in range(N)]
deq = deque()
for i in range(min(N,M)//2):
    # 1차원 배열로 변환
    deq.clear()
    deq.extend(A[i][i:M-i]) # 위쪽
    deq.extend([row[M-i-1] for row in A[i+1:N-i-1]]) # 오른쪽
    deq.extend(A[N-i-1][i:M-i][::-1]) # 아래쪽
    deq.extend([row[i] for row in A[i+1:N-i-1]][::-1]) # 왼쪽

    deq.rotate(-R)

    # 다시 2차원 배열로 변환
    for j in range(i, M-i): # 위쪽
        result[i][j] = deq.popleft()
    for j in range(i+1, N-i-1): # 오른쪽
        result[j][M-i-1] = deq.popleft()
    for j in range(M-i-1, i-1, -1): # 아래쪽
        result[N-i-1][j] = deq.popleft()
    for j in range(N-i-2, i, -1):   # 왼쪽
        result[j][i] = deq.popleft()

for line in result:
    print(*line)

# Ref) https://velog.io/@leetaekyu2077/%EB%B0%B1%EC%A4%80-16926%EB%B2%88-%EB%B0%B0%EC%97%B4-%EB%8F%8C%EB%A6%AC%EA%B8%B0-1