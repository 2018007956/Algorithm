import sys
import bisect
input = sys.stdin.readline

def good(x, i, j):
    left = bisect.bisect_left(arr, x)
    right = bisect.bisect_right(arr, x)
    return [idx for idx in range(left, right) if idx!=i and idx!=j]

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if good(arr[i]-arr[j], i, j):
            cnt += 1
            break
print(cnt)


#### 투포인터
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

## 방법1)
cnt = 0
for i in range(n):
    goal = arr[i]
    start, end = 0, n-1
    while start < end:
        if arr[start] + arr[end] == goal:
            # 값이 음수, 0도 될 수 있어서 아래 로직 필요
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif arr[start] + arr[end] > goal:
            end -= 1
        elif arr[start] + arr[end] < goal:
            start += 1

print(cnt)

## 방법2)
cnt = 0
for i in range(n):
    temp = arr[:i] + arr[i+1:]
    start, end = 0, n-2
    while start < end:
        if temp[start] + temp[end] == arr[i]:
            cnt += 1
            break
        elif temp[start] + temp[end] > arr[i]:
            end -= 1
        elif temp[start] + temp[end] < arr[i]:
            start += 1

print(cnt)