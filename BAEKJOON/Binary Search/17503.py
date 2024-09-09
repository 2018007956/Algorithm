# Solved (1h 34m)
import sys
import heapq
input = sys.stdin.readline
N, M, K = map(int, input().split())
beer = []
for _ in range(K):
    v, c = map(int, input().rstrip().split())
    beer.append((v, c))

beer.sort(key=lambda x:x[1])

select = beer[:N]
heapq.heapify(select)
cur_idx = N
cur_sum = sum([v for v, c in select])
while True:
    # print('--',select, cur_sum)
    if cur_sum >= M:
        print(beer[cur_idx-1][1])
        break
    else:
        if cur_idx == K:
            print(-1)
            break
        cur_sum -= heapq.heappop(select)[0]
        heapq.heappush(select, beer[cur_idx])
        cur_sum += beer[cur_idx][0]
        cur_idx += 1
'''
# Line 13~29가 더 최적화된 코드
select = []
cur_sum = 0
min_level = float('inf')

for i in range(K):
    heapq.heappush(select, beer[i][0])
    cur_sum += beer[i][0]

    if len(select) > N:
        cur_sum -= heapq.heappop(select)

    if len(select) == N and cur_sum >= M:
        min_level = min(min_level, beer[i][1])

print(min_level if min_level != float('inf') else -1)
'''
'''
12:43~1:49 (1h 6m) python, pypy 1% 시간초과
    v들의 합이 M 이상이되면서 c가 최대인 값
    시간 초과에 안걸리도록 조합을 어떻게 만들지?
    정렬해서 그리디로 확인, 최소값 만족하면 바로 종료

    조합의 개수가 매번 N으로 달라져서, 로직을 어떻게 짜야할지 고민. combination 밖에 안떠오름
    정렬을 어떻게 쓸 수 있을까?
    c 기준 정렬해서 N개씩 확인하고, M보다 작으면 최소값 pop, 그 다음 값 push

~2:17 (28m) Solved
    최적화 방법
    1. 선호도 합계를 매번 계산하지 않고 관리하기
        cur_sum 변수 만들어서 pop, push 할 때 같이 계산
    2. K 개까지 한번씩만 확인하면 되므로 while 대신 for i in range(K) 사용
'''