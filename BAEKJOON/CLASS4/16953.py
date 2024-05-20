# Solved (38m)
from collections import deque
A, B = map(int, input().split())
queue = deque([(A,1)])
while queue:
    x = queue.popleft()
    if x[0] > B:
        continue
    if x[0] == B:
        print(x[1])
        break

    if x[0]*2 <= B:
        queue.append((x[0]*2,x[1]+1))
    num = int(str(x[0])+'1')
    if num <=B:
        queue.append((num,x[1]+1))
else:
    print(-1)
'''
10:32~42 (10m) 메모리 초과
~57 (15m) 재귀로 풀어봤는데 잘 안됨
A, B = map(int, input().split())
cnt = 0
def recursion(x):
    global cnt
    if x<=B:
        if x==B:
            print(cnt)
            return
        else: 
            cnt += 1
            if x*2<=B:
                recursion(x*2)
            if int(str(x)+'1') <= B:
                recursion(int(str(x)+'1'))
recursion(A)

~10 (13m) bfs 알고리즘 개선, Solved
x2, 1추가 연산을 하게되면 같은 곳을 다시 방문하는 일은 없음. visited 제거
'''