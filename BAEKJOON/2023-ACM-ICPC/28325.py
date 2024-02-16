# 호숫가의 개미굴 - 성공
import math

N = input()
C = list(map(int, input().split()))

cnt_possible = []
cnt = 0 
if C == [0 for x in range(int(N))]: 
    cnt=-1
for idx, x in enumerate(C):
    if idx!=0 and x!=0:
        cnt_possible.append(cnt)
        cnt = 0        
    elif idx==len(C)-1:
        cnt+=1
        cnt_possible.append(cnt)
    elif x==0:
        cnt+=1

# 원형 배열 고려 - 앞뒤가 모두 0인 경우
if C[0]==C[-1]==0 and len(cnt_possible)>1:
    cnt_possible[0]+=cnt_possible.pop()

result = sum(C)
for i in cnt_possible:
    result += math.ceil(i/2)

print(result)