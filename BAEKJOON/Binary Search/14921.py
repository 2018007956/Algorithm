# Solved (26m) w/ Search
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

start = 0
end = N-1
ans = A[start] + A[end]
while start < end:
    cur = A[start] + A[end]
    if abs(ans) > abs(cur):
        ans = cur
    else:
        if cur < 0:
            start += 1
        else:
            end -= 1
print(ans)