# 풀이 공부
n = int(input()) # city
m = int(input()) # bus
cost = [[1e9] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                cost[a][b] = 0
            else:
                cost[a][b] = min(cost[a][b], cost[a][k]+cost[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if cost[a][b] == 1e9:
            print('0', end=' ')
        else:
            print(cost[a][b], end=' ')
    print()