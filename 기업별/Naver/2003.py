# Solved (8m)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_list = [0]
for a in A:
    sum_list.append(sum_list[-1] + a)

cnt = 0
for i in range(N+1):
    for j in range(i, N+1):
        if sum_list[j]-sum_list[i] == M:
            cnt += 1

print(cnt)
'''
10:00~07 (8m) Python 2% 시간 초과, PyPy Solved
    N 범위가 10000까지인데 왜 시간초과가 발생하나?
'''