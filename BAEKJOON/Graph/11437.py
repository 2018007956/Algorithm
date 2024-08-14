# Solved (30m) w/ Search
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1)
level = [0] * (N+1)
visited = [False] * (N+1)
def dfs(x, l):
    visited[x] = True
    level[x] = l

    for adj in graph[x]:
        if not visited[adj]:
            parent[adj] = x
            dfs(adj, l+1)            

# 가까운 공통 조상 찾기
def lca(a, b):
    # 깊이 맞추기
    while level[a] != level[b]:
        if level[a] > level[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 노드 맞추기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

dfs(1, 0)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))

'''
12:04~20, 31~46 (30m) python 93% 시간초과, pypy 제출 성공
'''