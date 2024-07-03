# 풀이 공부
def multi(a, b):
    cal = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                cal[i][j] += a[i][k] * b[k][j] % 1000
    return cal

def square(x, n):
    if n==1:
        return x

    tmp = square(x, n//2)
    if n%2==0:
        return multi(tmp, tmp)
    else:
        return multi(multi(tmp, tmp), x)


N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = square(A, B)
for i in range(N):
    for j in range(N):
        result[i][j] %= 1000

for k in result:
    print(*k)