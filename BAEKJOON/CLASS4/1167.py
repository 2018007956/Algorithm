# Solved (28m)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1, 2):
        n, w = arr[i],arr[i+1]
        tree[arr[0]].append((n, w))
        tree[n].append((arr[0],w))

tree = [set(x) for x in tree]

def dfs(start, distance):
    for next, next_w in tree[start]:
        if visited[next] == -1:
            visited[next] = distance + next_w
            dfs(next, visited[next])


visited = [-1] * (V+1)
visited[1] = 0
dfs(1, 0)
last_node = visited.index(max(visited))

visited = [-1] * (V+1)
visited[last_node] = 0
dfs(last_node, 0)
print(max(visited))

'''
9:44~10:6 (22m) 45% 시간 초과
    입력 받는 부분에서 매번 값이 존재하는지 체크하는 부분에서 시간이 많이 걸리는 것 같다
    체크하지 말고 일단 다 받고 난 다음 중복 제거

~10:12 (6m) Solved
'''