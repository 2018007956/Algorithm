# Solved (6m)
M, N = map(int, input().split())
space = []
for _ in range(M):
    coords = list(map(int, input().split()))
    rank = {val:i for i, val in enumerate(sorted(coords))}
    normalized = [rank[val] for val in coords]
    space.append(tuple(normalized))

ans = 0
for i in range(M-1):
    for j in range(i+1, M):
        if space[i] == space[j]:
            ans += 1
print(ans)