# Solved (40m) w/ Search
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
size = [int(input()) for _ in range(N)]

start, end = 1, max(size)
res = 0
while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for x in size:
        cnt += x//mid

    if cnt >= K:
        res = mid
        start = mid + 1
    else:
        end = mid -1

print(res)
'''
용량으로 이분탐색 하는게 아니라, 총 몇 명에게 나누어 줄 수 있는지를 카운트하여
최대한 많이 나누어 줄 수 있는 수를 계산

용량을 계산(cur += mid*(x//mid))하니까 이분 탐색 조건이 애매했음

95% 런타임 에러 (ZeroDivisionError)
    start = 0 으로 하면 0으로 나눠질 수 있으므로 start = 1
    주전자 용량이 모두 0으로 주어지는 경우는 이분탐색 할 필요 없이 바로 res 출력
'''