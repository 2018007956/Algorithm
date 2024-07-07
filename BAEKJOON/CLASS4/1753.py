# Solved (17m)
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    weight[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if dist > weight[node]:
            continue

        for adj_v, adj_w in graph[node]:
            if dist + adj_w < weight[adj_v]:
                weight[adj_v] = dist + adj_w
                heapq.heappush(q, (weight[adj_v], adj_v))


V, E = map(int, input().split())
K = int(input()) # start node

visited = [False] * (V+1)
weight = [1e9] * (V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)

for w in weight[1:]:
    if w == 1e9:
        print('INF')
    else:
        print(w)