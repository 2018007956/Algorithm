# Not Solved
import heapq as hq
from collections import deque
def solution(program):
    program = deque(sorted(program, key=lambda x: (x[1], x[0])))
    answer = [0] * 11
    ready_q = []
    now = 0
         
    def push():
        while program and program[0][1] <= now:
            hq.heappush(ready_q, program.popleft())
        
    while program or ready_q:
        if not ready_q:
            now = program[0][1]
            push()
            
        a, b, c = hq.heappop(ready_q)
        answer[a] += (now - b)
        now += c
        push()
    
    answer[0] = now
    return answer