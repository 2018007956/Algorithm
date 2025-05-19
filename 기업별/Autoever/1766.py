''' 위상 정렬(Topological Sort)
어떤 일을 하는 순서를 찾는 알고리즘
즉, 방향 그래프에 존재하는 각 정점들의 선행 순서를 위배하지 않으면서 모든 정점을 나열하는 것
'''
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N+1) # 위상 순서
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

print(graph)
print(indegree)
# [[], [], [], [1], [2]]
# [0, 1, 1, 0, 0]

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