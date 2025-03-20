# Solved (15m)
import math
def solution(progresses, speeds):
    times = []
    for x, spe in zip(progresses, speeds):
        times.append(math.ceil((100-x)/spe))
        
    answer = []
    idx = 0
    while idx < len(times):
        cur = times[idx]
        cnt = 1
        for i in range(idx+1, len(times)):
            if times[i] <= cur:
                cnt += 1
            else:
                break
        answer.append(cnt)
        idx += cnt
    return answer


# 다른 사람 풀이
def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s), 1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]