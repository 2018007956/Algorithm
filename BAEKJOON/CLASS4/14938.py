# Solved (19m)
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
num_of_items = list(map(int, input().split()))
graph = [[1e9] * (n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

# floyd warshall
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a==b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][k]+graph[k][b], graph[a][b])

regions = []
for a in range(1, n+1):
    can_get_items = 0
    for b in range(1, n+1):
        if graph[a][b] <= m:
            can_get_items += num_of_items[b-1]
    regions.append(can_get_items)

print(max(regions))