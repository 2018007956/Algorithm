# Solved
import heapq as hq
def solution(jobs):
    jobs.sort() # 요청 시간 기준 정렬
    queue = []
    cur_time, total, cnt, i = 0, 0, 0, 0
    n = len(jobs)
    
    while cnt < n:
        # 현재 시간 이하 요청 작업 힙에 추가
        while i < n and jobs[i][0] <= cur_time:
            hq.heappush(queue, (jobs[i][1], jobs[i][0], i))
            i += 1
            
        if queue:
            t, s, _ = hq.heappop(queue)
            cur_time += t
            total += cur_time-s
            cnt += 1
        else:
            # 현재 처리 가능한 작업이 없으면 다음 작업 요청 시간으로 이동
            cur_time = jobs[i][0]
            
    return total // n

# Not Solved
import heapq as hq
def solution(jobs):
    queue = []
    for i, (start, time) in enumerate(jobs):
        hq.heappush(queue, (time, start, i))
    
    result = []
    cur_time = 0
    while queue:
        t, s, i = hq.heappop(queue)
        cur_time += t
        if s > cur_time:
            cur_time += s-cur_time
        result.append(cur_time-s)
    
    return sum(result)//len(result)
'''
문제점 : , "현재 처리 가능한 작업 중에서 가장 짧은 작업"을 골라야 하는데, 코드는 "전체 작업 중 가장 짧은 작업"을 우선 선택하고 있음
정확한 풀이 접근 방법 : SJF + 최소힙
'''