# Solved (10m)
n = int(input())

start, end = 0, n
while start <= end:
    mid = (start + end) // 2

    if mid **2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start) # 제곱근 보다 크거나 같은 최소 정수 값