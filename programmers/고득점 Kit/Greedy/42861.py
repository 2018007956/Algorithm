# Solved
def kruskal(n, graph):
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

    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    ret = 0
    for a, b, w in graph:
        if find(a) != find(b):
            union(a, b)
            ret += w

    return ret


def solution(n, costs):
    graph = []
    for a, b, w in costs:
        graph.append((a, b, w))

    graph.sort(key=lambda x:x[2])
    return kruskal(n, graph)