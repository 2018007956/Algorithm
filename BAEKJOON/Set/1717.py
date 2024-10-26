# Disjoint set 분리집합
# Solved (21m) w/ Search
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])    
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    # 작은 트리를 큰 트리에 연결
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    command, a, b = map(int, input().split())
    if command==0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
'''
11:22~29 (7m) 2% 메모리초과
    각 노드를 개별 집합으로 관리하는 대신
    Union-Find 자료구조를 사용해 메모리를 절약하고 효율적으로 풀이할 수 있음

~43 (14m) union-find 풀이공부 
'''