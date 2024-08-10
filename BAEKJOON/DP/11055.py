# Solved (10m)
N = int(input())
A = list(map(int, input().split()))

dp = [[A[0], A[0]]]
for x in A[1:]:
    lst = [a for a in dp if a[0] < x]
    if lst:
        dp.append([x, max(lst, key=lambda x:x[1])[1]+x])
    else:
        dp.append([x, x])

print(max([x[1] for x in dp]))