# Solved (31m) w/ Search
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, K = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    start, end = 0, n-1
    min_diff = 1e9
    cnt = 0
    while start < end:
        cur_diff = abs((arr[start]+arr[end]) - K)

        if cur_diff < min_diff:
            min_diff = cur_diff
            cnt = 1
        elif cur_diff == min_diff:
            cnt += 1
        
        if arr[start]+arr[end] < K:
            start += 1
        else:
            end -= 1
    
    print(cnt)

'''
10:59~15 (16m) 1% 메모리초과
    arr_sum을 만들지 않고 계산하면서 탐색

~30 (15m) Solved
'''