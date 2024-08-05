# Solved (43m)
import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        result.append(x)
        for adj in graph[x]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                queue.append(adj)

    print(*result)    


N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

topology_sort()

'''
9:40~10:01 (21m) 링크드리스트로 구현
    python 3% 시간 초과, pypy 바로 시간 초과

10:27~10:44 (17m) 위상 정렬 공부
~49 (5m) Solved
'''