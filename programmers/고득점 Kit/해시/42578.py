# Solved
from collections import defaultdict
def solution(clothes):
    dict = defaultdict(int)
    for name, sort in clothes:
        dict[sort] += 1
    
    answer = 1
    for v in dict.values():
        answer *= v+1
    return answer-1

# 수학적으로 확률을 떠올리며 접근했으면 금방 풀렸을듯