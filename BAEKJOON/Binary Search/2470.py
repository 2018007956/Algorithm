# Solved (12m)
import sys
input = sys.stdin.readline
N = int(input())
value = list(map(int, input().split()))

value.sort()
closest_zero = float('inf')
start, end = 0, N-1
res = []
while start < end:
    cur = value[start] + value[end]

    if abs(cur) < closest_zero:
        closest_zero = abs(cur)
        res = [value[start], value[end]]

    if cur < 0:
        start += 1
    else:
        end -= 1

print(*res)
'''
2:17~27 (10m) 1% 틀렸습니다
    이분 탐색 조건이 abs(cur) < 0 로 되어있었는데, 이 조건을 만족시키는 경우는 없음 abs 제거

37~39 (2m) Solved
'''