import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a==b:
        return
    
    if rank[a] == rank[b]:
        parent[b] = a
        rank[a] += 1
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        return 

n = int(input())
planets = []
graph = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((i, x, y, z))

for dim in range(1, 4):
    planets.sort(key=lambda x:x[dim])
    for i in range(n-1):
        cost = abs(planets[i][dim] - planets[i+1][dim])
        graph.append((cost, planets[i][0], planets[i+1][0]))

graph.sort()

parent = [i for i in range(n)]
rank = [0] * n
min_cost = 0
for w, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        min_cost += w    
print(min_cost)

"""
kruskal algorithm 시간 복잡도 : O(ElogE), E는 간선의 개수
이 문제에서는 임의의 두 노드 사이에 터널을 연결할 수 있다고 가정하므로,
간선의 개수는 N(N-1)/2개이다.

N이 최대 100,000이므로, 모든 두 행성 간의 거리를 확인하는 방법은 시간 초과
터널의 비용이 min(|Xa - Xb|, |Ya - Yb|, |Za - Zb|)라고 정의되어 있고,
이 특징을 이용하면 고려할 간선의 개수를 줄일 수 있다.

=> x, y, z축을 기준으로 각각 정렬을 수행하고, 특정 축 기준으로 인접한 행성끼리만 고려한다.
총 간선의 개수는 3 * (N-1) 개가 되기 때문에 시간 초과가 해결된다.

* 주의 *
처음엔 아래 코드와 같이 최소 거리인 행성을 구해서 그래프로 만들었는데,
for i in range(n-1):
    cur_min = 1e8
    min_idx = ()
    for j in range(i+1, n):
        c = cost(planets[i], planets[j])
        if c < cur_min:
            cur_min = c
            min_idx = (i, j)
    graph.append((min_idx[0], min_idx[1], cur_min))

이렇게되면 전체가 연결되지 않은 그래프가 만들어질 수 있음
"""

# [ 핵심 아이디어 ] 
# 각 축(x, y, z)에 대해 정렬하고 인접 노드끼리만 연결해도
# MST에 포함될 수 있는 모든 중요한 간선들이 포함됨