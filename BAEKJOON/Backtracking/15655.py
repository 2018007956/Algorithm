# Solved (40m) 
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []
def dfs(depth):
    if len(s)==M:
        print(' '.join(map(str, s)))
        return

    for i in range(depth,N):
        if arr[i] not in s:
            s.append(arr[i])
            dfs(i+1) 
            s.pop()
            
dfs(0)
'''
dfs 호출할 때 depth+1 이 아니라 i+1 
    depth+1로 해주면, depth=0일 때 모든 index에 대해서 각각 1~3번째 수를 돌게 되므로 중복 결과 발생
'''


# Solved (3m)
from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for x in sorted(combinations(arr, M)):
    print(*x)