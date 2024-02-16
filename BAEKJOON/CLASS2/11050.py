from itertools import combinations
N, K = map(int, input().split())
print(len(list(combinations(range(N), K))))

'''
이항계수(binomial coefficient)
: n개의 서로다른 것들 중 k개를 선택하는 조합의 경우의 수
'''