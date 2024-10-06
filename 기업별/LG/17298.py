# 풀이 공부
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
NGE = [-1] * N
stack = [0] # 구해야 할 값의 index 저장

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)
    
print(*NGE)