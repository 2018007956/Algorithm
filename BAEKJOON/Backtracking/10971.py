# 풀이 공부
def dfs(depth, x):
    global sum_cost, min_cost
    if depth == N-1:
        if W[x][0]:
            sum_cost += W[x][0]
            min_cost = min(min_cost, sum_cost)
            sum_cost -= W[x][0]
        return

    for i in range(1, N):
        if not visited[i] and W[x][i]:
            visited[i] = True
            sum_cost += W[x][i]
            dfs(depth+1, i)
            visited[i] = False
            sum_cost -= W[x][i]


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
sum_cost = 0
min_cost = float('inf')

dfs(0, 0)
print(min_cost)