# 풀이 공부
N, K = map(int, input().split())
use = list(map(int, input().split()))

code = []
cnt = 0
for i in range(K):
    # 코드에 이미 꽂혀져 있는 경우
    if use[i] in code:
        continue

    # 코드에 자리가 남은 경우
    if len(code) < N:
        code.append(use[i])
        continue

    # 남은 사용 중에 가장 늦게 사용되는 것 뽑기
    priority = []
    for c in code: # 꽂혀져 있는 코드를
        if c in use[i:]: # 다음에 또 이용해야한다면
            priority.append(use[i:].index(c))
        else: # 이후 사용되지 않는 용품은 가장 먼저 뽑힐 수 있도록 처리
            priority.append(101) 
    target = priority.index(max(priority))
    code.remove(code[target])
    code.append(use[i])
    cnt += 1

print(cnt)