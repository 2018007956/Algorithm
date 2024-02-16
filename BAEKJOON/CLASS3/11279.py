import sys
import heapq as hq
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    num = int(input())
    if num == 0:
        if arr:
            print(hq.heappop(arr)[1])
        else:
            print(0)
    else:
        hq.heappush(arr, (-num, num)) # Max heap: (우선 순위, 값)

'''
heapq 모듈은 min heap으로 동작하기 때문에 max heap으로 활용하려면
각 값에 대한 우선순위를 구한 후, (우선 순위, 값) 구조의 튜플을 힙에 추가하거나 삭제함
그러면 튜플 내 맨 앞에 있는 값을 기준으로 최소 힙을 구성
힙에서 값을 읽어올 때는 [1]에 있는 값을 취하면 됨
'''