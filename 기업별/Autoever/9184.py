# def w(a, b, c):
#     if a<=0 or b<=0 or c<=0:
#         return 1
    
#     if a>20 or b>20 or c>20:
#         return w(20, 20, 20)
    
#     if a<b and b<c:
#         return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
#     else:
#         return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

## >> 위 재귀함수에서 DP 사용으로 시간 단축
def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    
    if dp[a][b][c]:
        return dp[a][b][c]

    if a<b and b<c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    return dp[a][b][c]

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, input().split())
    if a==b==c==-1:
        break

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')