# Solved (13m)
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

def topology_sort():
    result = []
    queue = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(queue, i)

    while queue:
        queue.sort()
        x = heapq.heappop(queue)
        result.append(x)
        for adj in graph[x]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                heapq.heappush(queue, adj)

    print(*result)

topology_sort()

'''
1:03~13 (10m) 8% 시간초과
~16 (3m) deque 대신 heapq 사용 Solved
'''