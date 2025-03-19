# Solved (6m)
from collections import defaultdict
def solution(participant, completion):
    dict = defaultdict(int)
    for x in participant:
        dict[x] += 1
    for x in completion:
        dict[x] -= 1
    return sorted(dict.items(), key=lambda x:x[1])[-1][0]


# 다른 사람 풀이) Counter 사용
from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


# 다른 사람 풀이) Hash 사용
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer