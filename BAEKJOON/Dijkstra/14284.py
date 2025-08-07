import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = hq.heappop(q)
        if now == t:
            break

        if distance[now] < dist:
            continue

        for adj_v, adj_w in graph[now]:
            if dist + adj_w < distance[adj_v]:
                distance[adj_v] = dist + adj_w
                hq.heappush(q, (dist+adj_w, adj_v))


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [1e8] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())

dijkstra(s)
print(distance[t])