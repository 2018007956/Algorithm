# 풀이 공부
S, C = map(int, input().split())
L = [int(input()) for _ in range(S)]

start, end = 1, max(L)
while start <= end:
    mid = (start + end) // 2

    cur = sum(x//mid for x in L)
    if cur >= C:
        start = mid+1
    else:
        end = mid-1

print(sum(L) - (C * end))