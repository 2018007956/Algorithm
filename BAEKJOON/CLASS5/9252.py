# Solved (28m)
a = input()
b = input()
LCS = [[0] * (len(b)+1) for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])

route = []
i, j = len(a), len(b)
if LCS[-1][-1] > 0:
    while i>0 and j>0:
        if a[i-1] == b[j-1]:
            route.append(a[i-1])
            i-=1
            j-=1
        else:
            if LCS[i-1][j] > LCS[i][j-1]:
                i-=1
            else:
                j-=1

route.reverse()
print(''.join(route))