# Solved (7m)
N = int(input())
P = list(map(int, input().split()))

P.sort()

cumulate = [0]
for i in range(N):
    cumulate.append(cumulate[i]+P[i])

print(sum(cumulate))