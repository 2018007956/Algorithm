# Solved (34m)
import math

def comb(n, r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

n = int(input())
result = 0
for r in range(n//2+1):
    result += comb(n, r) 
    n -=1
print(result%10007)

'''
11:22~48 (24m) 틀렸습니다
2:11~21 (10m) 
Ref) https://www.acmicpc.net/board/view/128186
틀린 원인 : 실수 오차
-> // 사용하여 정수로 연산하여 Solved
'''

# 또 다른 풀이
n = int(input())
dp = [1, 2]
for i in range(2, n):
    dp.append(dp[i-2]+dp[i-1])
print(dp[n-1]%10007)