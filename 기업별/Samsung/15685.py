# 풀이 공부
N = int(input())

graph = [[0] * 101 for _ in range(101)]
move = [(0,1), (-1,0), (0,-1), (1,0)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    graph[y][x] = 1

    curve = [d]
    for i in range(g):
        for j in range(len(curve)-1, -1, -1):
            curve.append((curve[j]+1) %4)

    for i in range(len(curve)):
        y += move[curve[i]][0]
        x += move[curve[i]][1]
        if x < 0 or x > 100 or y < 0 or y > 100:
            continue

        graph[y][x] = 1


cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            cnt += 1

print(cnt)
