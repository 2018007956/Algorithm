# 풀이 공부
from collections import defaultdict
T = int(input())
for _ in range(T):
    W = input()
    K = int(input())

    dic = defaultdict(list)

    for i in range(len(W)):
        if W.count(W[i]) >= K: # 개수가 K개 이상인 문자들에 대해서
            dic[W[i]].append(i) # 좌표값 저장

    if not dic:
        print(-1)
    else:
        small = 10000
        big = 1
        for alpha in dic:
            for i in range(len(dic[alpha])-K+1):
                length = dic[alpha][i+K-1] - dic[alpha][i] + 1

                small = min(small, length)
                big = max(big, length)

        print(small, big)

'''
4:53~24 (30m) 

~40 (16m) 풀이 공부
    특정 문자가 어느 곳에서 등장하는지를 딕셔너리를 통해 저장
    문자열의 길이 = 특정 문자의 좌표들간의 간격 + 1
'''