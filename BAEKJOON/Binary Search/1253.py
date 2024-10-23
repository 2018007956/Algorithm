# Solved (1h) w/ Search
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
'''
2:31~43 (12m) python 시간초과 pypy 10% 틀렸습니다
    다른 두 수의 합으로 나타낸다는 조건 -> if i==j: continue

    return right-left (X)
    return [idx for idx in range(left, right) if idx!=i and idx!=j] (O)
    => 숫자가 존재해서 right-left가 1이어도 i나 j에 해당하는 값이어서 두 수의 합으로 만들 수 없을 수 있음

~55, 10:17~59 (54m) Solved
'''