# Solved (30m) w/ Search 
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    cost[start] = 0
    while queue:
        dist, cur = heapq.heappop(queue)
        if dist > cost[cur]:
            continue

        for adj_n, adj_w in graph[cur]:
            if dist + adj_w < cost[adj_n]:
                cost[adj_n] = dist + adj_w
                route[adj_n] = cur # 이전 간선 기억
                heapq.heappush(queue, (cost[adj_n], adj_n))


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
start, end = map(int, input().split())

cost = [1e9] * (n+1)
route = [-1] * (n+1)
route[start] = start
dijkstra(start)
print(cost[end])

# trace
path = [end]
now = end
while now != start:
    now = route[now]
    path.append(now)

path.reverse()

print(len(path))
print(*path)