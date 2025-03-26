# Solved (20m)
from collections import defaultdict
import math
def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5] * math.ceil(len(answers)/5)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(len(answers)/8)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(len(answers)/10)
    score = defaultdict(int)
    for i, ans in enumerate(answers):
        if one[i]==ans:
            score[1] += 1
        if two[i]==ans:
            score[2] += 1
        if three[i]==ans:
            score[3] += 1
            
    for student, score in sorted(score.items(), key=lambda x:x[1], reverse=True):
        if not answer or answer[-1][1]==score:
            answer.append((student, score))
        else:
            break        
    return sorted([x[0] for x in answer])


# 다른 사람 풀이
# -> defaultdict말고 list로 고정된 index로 카운팅하면 정렬 필요 없음
def solution(answers):
    answer = []
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i, ans in enumerate(answers):
        if pattern1[i%len(pattern1)]==ans:
            score[0] += 1
        if pattern2[i%len(pattern2)]==ans:
            score[1] += 1
        if pattern3[i%len(pattern3)]==ans:
            score[2] += 1
            
    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx+1)
    return answer