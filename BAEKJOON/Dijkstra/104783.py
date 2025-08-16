# Not Solved
import sys
import heapq as hq
input = sys.stdin.readline

def dist(cx, cy, nx, ny):
    return ((cx - nx)**2 + (cy - ny)**2) **0.5

def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue

        for adj_v, adj_w in enumerate(graph[now]):
            if dist + adj_w < distance[adj_v]:
                distance[adj_v] = dist + adj_w
                hq.heappush(q, (dist+adj_w, adj_v))


cx, cy = map(float, input().split())
dx, dy = map(float, input().split())
n = int(input())

cannon = [(cx, cy)]
for _ in range(n):
    x, y = map(float, input().split())
    cannon.append((x, y))
cannon.append((dx, dy))

# 점과 점 사이에 걸리는 시간을 값으로 하는 array를 만들어서 Dijkstra
# graph[i][j] : i→j로 이동하는 데 걸리는 시간
graph = [[] for _ in range(n+2)]
distance = [1e8] * (n+2)
for i in range(n+2):
    for j in range(n+2):
        d = dist(cannon[i][0], cannon[i][1], cannon[j][0], cannon[j][1])
        if i==0 or i==len(cannon)-1:
            # 걸어가는 시간
            graph[i].append(d/5)
        else:
            # 대포 한 번 + 걸어가기
            graph[i].append(abs(d-50)/5+2)

dijkstra(0)
print(distance[len(cannon)-1])