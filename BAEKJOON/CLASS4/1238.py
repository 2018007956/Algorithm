# Solved (30m)
import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    weight[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if dist > weight[node]:
            continue

        for adj_n, adj_w in graph[node]:
            if dist + adj_w < weight[adj_n]:
                weight[adj_n] = adj_w + dist
                heapq.heappush(q, (weight[adj_n], adj_n))


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e,t))

# 목적지로 가는 시간 계산
time = []
for i in range(1, N+1):
    weight = [1e9] * (N+1)
    dijkstra(i)
    time.append(weight[X])
# 짐으로 돌아오는 시간 계산
weight = [1e9] * (N+1)
dijkstra(X)
print(max([go+back for go, back in zip(time,weight[1:])]))