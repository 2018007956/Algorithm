def dfs(depth, x, cost):
    global min_cost
    if depth==N-1:
        min_cost = min(min_cost, cost+weight[x][0])
        return 

    for i in range(1, N):
        if not visited[i] and weight[x][i]:
            visited[i] = True
            dfs(depth+1, i, cost+weight[x][i])
            visited[i] = False


N = int(input())
weight = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_cost = 1e8
dfs(0, 0, 0)
print(min_cost)

'''
for i in range(1, N) 에서 0을 꼭 빼줘야 함
그래야 바로 출발지로 돌아오지 않고 끝까지 돌다가 마지막에 0 방문 가능
'''