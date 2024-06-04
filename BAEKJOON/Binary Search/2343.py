# Solved (40m) w/ Search
N, M = map(int, input().split())
lecture = list(map(int, input().split()))

start, end = max(lecture), sum(lecture)
while start <= end:
    mid = (start+end) // 2

    cnt = 1
    total = 0
    for x in lecture:
        if total + x > mid:
            cnt += 1
            total = 0
        total += x

    if cnt <= M:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)

'''
hint : 이분 탐색 범위 설정 
    최소 크기 : 각 강의의 최대 길이 (블루레이 크기는 최소한 가장 긴 강의보다 커야 함)
    최대 크기 : 모든 강의의 길이의 합 (모든 강의를 하나의 블루레이에 담는 경우)
'''