# Solved (1h 26m) w/ Search
def mul(num, exp):
    if exp == 1:
        return num
    if exp%2 == 0:
        half = mul(num, exp//2)
        return half * half % X
    else:
        return num * mul(num, exp-1) % X

X = 1000000007
M = int(input())
result = 0
for _ in range(M):
    N, S = map(int, input().split())
    result += S*mul(N, X-2)%X

print(result % X)
'''
Q = 7/3 예시에서, 4가 어떻게 나온거지?
11:41~36 (55m) 풀이 감을 못잡아서 인터넷 참고
    N^(-1) * N = 1(mod X) = N^(X-1) => N^(-1) = N^(-1) (mod X) = N^(X-2)
    a*b^(-1) mod X = a*b^(X-2) mod X

    지수승 계산을 시간 내에 해야하는 문제 "Exponentiation by Squaring, 빠른 거듭제곱법" 이라는 것을 알았고,
    return mul(num, exp//2) * mul(num, exp//2) % X 이렇게 재귀를 통해 구현해주었지만
    출력 시간이 너무 오래 걸림
    => 위 코드를 아래와 같이 수정하였더니, 빠르게 출력됨
    half = mul(num, exp//2)
    return half * half % X
    => 재귀 호출의 중복 제거 (:동일한 계산을 반복하지 않도록 최적화하는 DP의 memoization 기법과 유사)
        첫 번째 코드는 같은 값을 여러 번 계산하게 되어 시간 복잡도 매우 증가
        두 번째 코드는 mul를 한 번만 호출하고, 그 결과를 재사용함으로써 중복 계산 제거됨

~1:07 (31m) Solved
'''