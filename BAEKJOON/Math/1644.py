# 풀이공부
N = int(input())

# 1. 에라토스테네스의 체 : 주어진 N까지의 소수를 미리 구한다
chk = [False, False] + [True] * (N-1)
prime_num = []
for i in range(2, N+1):
    if chk[i]:
        prime_num.append(i)
        # i의 배수 (2*i, 3*i, 4*i, ...) 소수가 아님을 표시
        for j in range(2*i, N+1, i):
            chk[j] = False

# 2. 투포인터
cnt = 0
start, end = 0, 0
while end <= len(prime_num):
    cur = sum(prime_num[start:end])
    if cur == N:
        cnt += 1
        start += 1
    elif cur < N:
        end += 1
    else:
        start += 1

print(cnt)