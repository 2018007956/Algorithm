# Solved (17m)
import copy
def solution(want, number, discount):
    d = {}
    for i in range(len(want)):
        d[want[i]] = number[i]
    
    cnt = 0
    for i in range(len(discount)-9):  # <- 이런 부분을 계산하는데 시간 소요됨 ####check
        d_copy = copy.deepcopy(d)      
        for x in discount[i:i+10]:
            if x in d_copy:
                d_copy[x] -= 1
        if all(x==0 for x in d_copy.values()):
            cnt += 1
    return cnt
'''
range(len(discount)-9) 이 부분에서 전혀 오래 생각할 필요 없음
    10자리씩 슬라이딩하는 경우, 뒤에서 10자리인 숫자까지 고려해줘야 하는데
    range는 해당 숫자의 -1값까지 고려되므로 +1 해줘야 함 (-10+1=-9)

다른 사람 풀이 : from collections import Counter 사용
if d==Counter(discount[i:i+10]):
    cnt += 1
'''