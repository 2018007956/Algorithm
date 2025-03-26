# Solved
# 특정 시작점에서 모든 노드까지 최단 경로 찾기 : 다익스트라
import heapq as hq
def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue
        for adj_v in graph[now]:
            if dist+1 < distance[adj_v]:
                distance[adj_v] = dist+1
                hq.heappush(q, (dist+1, adj_v))

def solution(n, edge):
    global distance, graph
    graph = [[] for _ in range(n+1)]
    distance = [1e8] * (n+1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    dijkstra(1)
    return distance.count(max(distance[1:]))


## 가중치가 동일한 그래프에서는 BFS를 활용하면 최적의 성능으로 최단거리를 찾을 수 있다
from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [-1] * (n+1) 

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # BFS
    queue = deque([1])
    distance[1] = 0  # 시작점 거리 초기화
    while queue:
        cur = queue.popleft()
        for neighbor in graph[cur]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[cur] + 1
                queue.append(neighbor)

    max_dist = max(distance)
    return distance.count(max_dist)