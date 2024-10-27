# 풀이 공부
import sys
from itertools import permutations
sys.setrecursionlimit(10**6)

def dfs(a,b,c):
    # 재방문
    if (a,b,c) in dp:
        return dp[(a,b,c)]

    # 종료
    if (a,b,c) == (0,0,0):
        return 0
    
    min_val = 1e9
    for x,y,z in permutations([9,3,1]):
        min_val = min(min_val, dfs(max(0, a-x), max(0, b-y), max(0, c-z))+1)

    dp[(a,b,c)] = min_val
    return min_val


N = int(input())
SCV = list(map(int, input().split()))
for _ in range(3-N):
    SCV.append(0)

dp = {}
print(dfs(*SCV))
'''
공격할 세 개의 SCV를 어떻게 뽑아야 할지
    permutation 사용

10:56~20, 35~40 (30m) 고민

4:00~33 풀이공부
'''