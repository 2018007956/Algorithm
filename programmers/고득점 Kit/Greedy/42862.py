# Solved
def solution(n, lost, reserve):
    lost_ = list(set(lost)-set(reserve))
    reserve_ = list(set(reserve)-set(lost))
    
    answer = n - len(lost_)
    for x in lost_:
        if x-1 in reserve_:
            answer += 1
            reserve_.remove(x-1)
        elif x+1 in reserve_:
            answer += 1
            reserve_.remove(x+1)
    return answer
'''
"자기 옷 있는 사람은 자기 옷 먼저 입는다"는 로직을 선반영해줘야 함
'''

# 코드 정리
def solution(n, lost, reserve):
    lost_ = list(set(lost)-set(reserve))
    reserve_ = list(set(reserve)-set(lost))
    
    for x in reserve_:
        if x-1 in lost_:
            lost_.remove(x-1)
        elif x+1 in lost_:
            lost_.remove(x+1)
    return n-len(lost_)