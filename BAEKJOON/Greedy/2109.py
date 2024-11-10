# 풀이 공부
import sys
import heapq as hq
input = sys.stdin.readline
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

# 날짜 순으로 정렬
schedule.sort(key=lambda x:x[1])

heapq = []
for p, d in schedule:
    hq.heappush(heapq, p)
    # 강연일보다 더 크다면 가장 작은 값 제거
    # 'X일 이내'이므로 작은 값이 큰 값에 포함되는 상황, pay가 큰 것들을 남김
    if d < len(heapq):
        hq.heappop(heapq)

print(sum(heapq))