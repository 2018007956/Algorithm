def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a<b<c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, input().split())
    if a==b==c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')

'''
재귀로 오래걸렸던 이유는 계속해서 동일한 값을 반복 연산하기 때문
-> dp값이 존재하면 return 해주면 연산속도 기하급수적으로 빨라짐
'''