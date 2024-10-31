# 풀이 공부
import sys
input = sys.stdin.readline
def kruskal():
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        
        if rank[a] == rank[b]:
            parent[b] = a
            rank[a] += 1
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[a] = b

    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    res = 0
    for a, b, w in graph:
        if find(a) != find(b):
            union(a, b)
            res += w

    print(res)
    

N = int(input())
M = int(input())
graph = []
for _ in range(M):
    a, b, w = map(int, input().split())
    graph.append((a, b, w))

graph.sort(key=lambda x: x[2])
kruskal()
'''
스패닝 트리 : 그래프 내의 모든 정점을 포함하고 사이클이 없는 트리
Minimum Spanning Tree (MST) : Kruskal, Prim

[Kruskal Algorithm]
구성한 스패닝 트리에 사이틀이 발생하는지에 대한 여부를 판단하기 위해 Disjoint Set 사용
동작 과정
1. 간선을 가중치를 기준으로 오름차순 정렬한다.
2. 간선을 순차적으로 순회하면서 최소 신장 트리를 만든다.
   이때, 서로소 집합 알고리즘에 기반하여 트리에 순환성이 생기지 않는 간선만 추가한다.
3. 최소 신장 트리가 될 때까지 2번 과정을 반복한다.

[Prim Algorithm]
그리디 알고리즘을 사용하여 인접한 간선의 가중치가 최소인 정점을 선택
동작 과정
1. 임의의 정점을 시작 정점으로 선택하여 최소 신장 트리를 만든다.
2. 삽입된 정점과 인접한 정점 중 연결된 간선의 가중치가 가장 작은 정점을 최소 신장 트리에 추가한다.
   이때, 방문한 노드를 다시 탐색하지 않도록 하여 트리에 순환성이 생기는 것을 방지한다.
3. 최소 신장 트리가 될 때까지 2번 과정을 반복한다.
'''