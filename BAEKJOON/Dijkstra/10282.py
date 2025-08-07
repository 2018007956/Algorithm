import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue

        for adj_v, adj_w in graph[now]:
            if dist + adj_w < distance[adj_v]:
                distance[adj_v] = dist + adj_w
                hq.heappush(q, (dist+adj_w, adj_v))


t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [1e8] * (n+1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    dijkstra(c)
    
    cnt, time = 0, 0
    for d in distance:
        if d != 1e8:
            cnt+=1
            time = max(time, d)

    print(cnt, time)