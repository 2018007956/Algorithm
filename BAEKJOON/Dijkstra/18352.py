import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    hq.heappush(q, start)
    distance[start] = 0

    while q:
        now = hq.heappop(q)
        for adj_v in graph[now]:
            if distance[now] + 1 < distance[adj_v]:
                distance[adj_v] = distance[now] + 1
                hq.heappush(q, adj_v)


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [1e8] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dijkstra(x)
cnt = 0
chk = False
for i, d in enumerate(distance):
    if d==k:
        print(i)
        chk = True

if chk==False:
    print(-1)