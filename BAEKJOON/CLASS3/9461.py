import sys
input = sys.stdin.readline

def pado(n):
    P = [0,1,1,1,2,2,3,4,5,7,9]
    if n <= 10:
        return P[n]
    else:
        for x in range(11,n+1):
            P.append(P[x-1]+P[x-5])
        return P[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(pado(N))

'''
**시간초과**
재귀를 사용해도 가능하지만 깊이가 깊어지면 과부하 걸림
<DP> 
기본적인 접근 방식: 분할 정복 알고리즘
-> 문제를 부분 문제로 나누어 각 부분 문제의 답을 계산하고 결과값을 이용해 원래 문제의 답을 산출
여기서 DP는 문제를 나눌 때 부분 문제를 최대한 많이 이용하도록 놔두고
주어진 부분 문제의 정답을 한번만 계산하고 저장해둔 뒤 (Cashing)
다시 한 번 해당 문제를 풀 때는 저장해둔 답을 바로 산출하여 속도를 향상한 것
<DP 구현 방법 2가지>
1. 하향식 Memoization (Memorization아님)
2. 상향식 Tabulation
'''