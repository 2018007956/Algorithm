# 풀이 공부
import sys
import heapq
input = sys.stdin.readline

def prim(s, w):
    queue = [[w, s]]
    visited = [False] * (V+1)
    ans = 0
    cnt = 0
    while cnt < V:
        w, s = heapq.heappop(queue)
        if not visited[s]:
            visited[s] = True
            ans += w
            cnt += 1
            for e, w in graph[s]:
                heapq.heappush(queue, (w, e))
    
    print(ans)


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

prim(1, 0)

'''
1:01~08 (7m) 
10:04~10:51 (47m) 최소 스패닝 트리 공부 및 문제 풀이

트리 : 사이클 없이 모든 정점이 연결된 그래프
스패닝 트리 : original graph와 같은 정점을 갖는 subgraph
최소 스패닝 트리 (Minimum Spanning Tree; MST) : 가중치 합이 최소인 스패닝 트리
MST 구하는 방법 :  Kruskal Algorithm, Prim Algorithm
'''