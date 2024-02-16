from collections import deque
N, K = map(int, input().split())

lst = deque(list(range(1,N+1)))
yosepus = []
cnt = 1
while lst:
    if cnt % K == 0:
        yosepus.append(lst.popleft())
    else:
        lst.append(lst.popleft())
    cnt += 1
    
print('<',end='')
for i in yosepus[:-1]:
    print(i,end=', ')
print(f'{yosepus[-1]}>')
'''
input: 7 3
1 2 3 4 5 6 7
output: <3, 6, 2, 7, 5, 1, 4>
'''