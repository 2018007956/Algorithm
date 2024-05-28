# Solved (41m) w/ search
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
tree = {}
for i in range(1, N+1):
    tree[i] = []

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
    
queue = deque([1])
parent = [0] * (N+1)
while queue:
    x = queue.popleft()
    for i in tree[x]:
        if parent[i] == 0:
            parent[i] = x
            queue.append(i)

for i in range(2, N+1):
    print(parent[i])