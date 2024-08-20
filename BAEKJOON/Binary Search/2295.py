# Solved (19m) w/ Search
import sys
input = sys.stdin.readline
N = int(input())
U = [int(input()) for _ in range(N)]

U.sort()

arr_sum = set()
for x in U:
    for y in U:
        arr_sum.add(x+y)

def check():
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            if U[i] - U[j] in arr_sum:
                return U[i]

print(check())

'''
11:44~56 (12m) python 시간 초과 pypy 2%? 시간초과
    max_val = 0
    for case in combinations(U[:-1], 3):
        idx = bisect.bisect_left(U, sum(case))
        if idx < len(U) and sum(case) == U[idx]:
            max_val = max(max_val, U[idx])
    print(max_val)

~12:05 (9m) 풀이 공부
    x + y + z = k 일 때, x + y = k - z 임을 이용
    1. arr_sum : 두 수의 합 (x + y)을 집합에 모두 넣어둔다. (두 수는 중복 가능)
    2. check : 탐욕적 접근으로 k가 가장 큰 수부터 오게 끔 역으로 접근
       k-z가 arr_sum에 존재한다면 (x+y = k-z), return k
'''