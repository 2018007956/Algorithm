# 풀이 공부
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))

min_len = 1e5
start, end = 0, 0
tmp = 0 
while True:
    if tmp >= S:
        min_len = min(min_len, end-start)
        tmp -= arr[start]
        start += 1
    elif end == N:
        break
    else:
        tmp += arr[end]
        end += 1

print(min_len if min_len != 1e5 else 0)