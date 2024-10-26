# 풀이 공부
from math import comb
def find_kth_permutation():
    global N, M, K
    result = []
    while N>0 and M>0:
        # 현재 첫 번째 자리에 'a'가 올 경우의 수
        count_a = comb(N-1+M, M)

        # 'a'가 올 수 있는 경우의 수 안에 포함되면
        if K <= count_a:
            result.append('a')
            N -= 1
        else:
            result.append('z')
            K -= count_a # 'a'로 시작하는 모든 경우의 수 제외하고 나머지 순열 중 K번째 찾음
            M -= 1

    # 남은 'a'와 'z'를 모두 추가
    result.extend('a' * N)
    result.extend('z' * M)

    return ''.join(result)


N, M, K = map(int, input().split())
if comb(N+M, M) < K:
    print(-1)
else:
    print(find_kth_permutation())
    
'''
조합론을 활용하여 순열을 모두 생성하지 않고 K번째 순열을 바로 찾아내기
math.comb(n, k)는 n개 중에서 k개를 고르는 경우의 수를 계산하는 함수
'''