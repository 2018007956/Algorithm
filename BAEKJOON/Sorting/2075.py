# Solved (16m) w/ Search
import sys
import heapq
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    if not arr:
        for num in tmp:
            heapq.heappush(arr, num)
    else:
        for num in tmp:
            if arr[0] < num: # 최솟값보다 현재 숫자가 클 경우 최소값 제거
                heapq.heappush(arr, num)
                heapq.heappop(arr)

arr.sort(reverse=True)
print(arr[N-1])
'''
5:54~57 (3m) 3% 메모리 초과
    arr의 길이를 계속 N만큼 유지

~10 (13m) 
'''