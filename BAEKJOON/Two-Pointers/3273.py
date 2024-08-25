# Solved (16m) w/ Search
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

cnt = 0
start, end = 0, n-1
while start < end:
    cur = arr[start] + arr[end]
    if cur == x:
        cnt += 1
        start += 1
    elif cur < x:
        start += 1
    else:
        end -= 1

print(cnt)

# Another Solution -> python, pypy 시간 초과
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

cnt = 0
for i in arr:
    if x-i in arr:
        cnt += 1

print(cnt//2)