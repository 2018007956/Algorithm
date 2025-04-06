# Solved
from collections import defaultdict
def solution(genres, plays):
    dict = defaultdict(list)
    dict_sum = defaultdict(int)
    for i, (g, p) in enumerate(zip(genres, plays)):
        dict[g].append([p, i])
        dict_sum[g] += p
    
    res = sorted(dict_sum.items(), key=lambda x:x[1], reverse=True)
    
    answer = []
    for k, v in res:
        tmp = sorted(dict[k], key=lambda x:x[0], reverse=True)
        answer.extend(list(zip(*tmp))[1][:2])
    return answer
'''
처음엔 노래의 index를 가져올 때 dict[g].append([p, plays.index(p)])로 구현했는데,
이러면 해당 재생 횟수를 가진 노래의 "첫 번째 인덱스"만 반환함
즉, 같은 재생 수를 가진 노래가 여러 개 있을 경우, 전부 같은 인덱스를 가지게 됨
=> 개선 : enumerate를 활용해서 index를 직접 받아오기
'''