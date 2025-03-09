# Solved (12m)
import heapq
n, m = map(int, input().split())
card = list(map(int, input().split()))

heapq.heapify(card)

cnt = 0
while cnt != m:
    x1 = heapq.heappop(card)
    x2 = heapq.heappop(card)
    heapq.heappush(card, x1+x2)
    heapq.heappush(card, x1+x2)
    cnt += 1

print(sum(card))