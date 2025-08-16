from collections import deque
def solution(menu, order, k):
    answer = 0
    
    queue = deque([])
    end = 0
    for i, drink in enumerate(order):
        
        while queue and queue[0] <= k * i:
            queue.popleft()
            
        end = max(end, k*i) + menu[drink]
        queue.append(end)
        
        answer = max(answer, len(queue))
        
        # print(k * i, queue)
    
    return answer

'''
간과한 부분
1. 완성 시각은 단순히 도착시간 + 제조시간이 아니라, 직전 작업의 완성 시각과 현재 도착 시각 중 큰 값에 제조시간을 더한 값
2. 큐에는 절대 종료시각을 넣고, 그 값을 기준으로 나간 손님을 제거
3. 새 손님이 k*i에 도착하면, t 이전에 끝난 손님들을 전부 제거하고, 그 다음 새 손님의 종료시간을 push
'''