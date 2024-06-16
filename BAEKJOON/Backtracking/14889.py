# 백트래킹 풀이 공부
import sys
input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_diff = 1e9
def dfs(depth, idx):
    global min_diff
    if depth==N//2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j] 
                elif not visited[i] and not visited[j]:
                    link += S[i][j] 
                
        min_diff = min(min_diff, abs(start-link))
        
    # 팀을 꾸리는 모든 경우의 수를 재귀를 통해 구함
    for i in range(idx, N): # 이미 선택된 인덱스를 다시 선택하지 않기 위해 idx 부터 시작
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0, 0)
print(min_diff)

''' 조합 풀이 Solved (22m) 
import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_diff = 1e9
for start in combinations(range(1, N+1), N//2):
    
    link = [x for x in range(1, N+1) if x not in start]

    start_score = 0
    link_score = 0
    for i, j in combinations(start, 2):
        start_score += S[i-1][j-1] + S[j-1][i-1]
    for i, j in combinations(link, 2):
        link_score += S[i-1][j-1] + S[j-1][i-1]

    min_diff = min(min_diff, abs(start_score - link_score))

print(min_diff)
'''