# Solved (20m) 
import sys
from itertools import combinations
input = sys.stdin.readline

def distance(A, B):
    cnt = 0
    for x, y in zip(A, B):
        if x!=y:
            cnt += 1
    return cnt

T = int(input())
for _ in range(T):
    N = int(input())
    mbti = input().split()

    if N>32:
        print(0)
    else:
        result = []
        for x, y, z in combinations(mbti, 3):
            result.append(distance(x,y)+distance(y,z)+distance(x,z))
        print(min(result))

'''
1:32~41 (9m) 시간초과 - 브루트포스
시간복잡도 : O(C(100000, 3)) = O(166,661,667,000,000)
~1:52 (11m) Solved - 비둘기집 원리 이용
N>32인 경우 무조건 같은 mbti 3명 존재
'''