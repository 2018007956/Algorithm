import sys
import heapq as hq
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    num = int(input())
    if num == 0:
        if arr:
            print(hq.heappop(arr))
        else:
            print(0)
    else:
        hq.heappush(arr, num)