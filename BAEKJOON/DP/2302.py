# 풀이 공부
N = int(input())
M = int(input())
VIP = [int(input()) for _ in range(M)]

dp = [0] * (N+1)
dp[0], dp[1] = 1, 1

# 점화식 계산
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

cnt = 1
# VIP의 유무에 따라 경우의 수를 도출
if M > 0:
    pre = 0
    # 반복문을 통해 VIP 사이 그룹에 들어가는 경우의 수를 확인
    for j in range(M):
        cnt *= dp[VIP[j]-1-pre]
        pre = VIP[j]
    cnt *= dp[N-pre]
else:
    cnt = dp[N]

print(cnt)
'''
위 알고리즘대로 하면
dp[3] * dp[2] * dp[2] 를 계산하게 됨

1 2 3 [4] 5 6 [7] 8 9
'''