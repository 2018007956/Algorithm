import sys
input = sys.stdin.readline

N, K = map(int, input().split())

A = []
for _ in range(N):
    x = int(input())
    if x > K:
        pass
    else:
        A.append(x)
        
cnt = 0
for i in sorted(A, reverse=True):
    cnt += K//i 
    K = K%i
    if K == 0:
        break
print(cnt)