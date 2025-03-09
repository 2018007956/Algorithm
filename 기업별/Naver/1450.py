# Not Solved
import sys
import bisect
from itertools import combinations
input = sys.stdin.readline
N, C = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort()

idx = bisect.bisect_right(weight, C)
cnt = 0
for i in range(C+1):
    cnt += len(list(combinations(weight[:idx], i)))
print(cnt)

# https://supersfel.tistory.com/entry/1450%EB%83%85%EC%83%89%EB%AC%B8%EC%A0%9C