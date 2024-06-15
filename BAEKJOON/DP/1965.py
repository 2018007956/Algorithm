# Solved (12m)
n = int(input())
box = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i, n):
        if box[i] < box[j]:
            dp[j] = max(dp[i]+1, dp[j])
print(max(dp))

'''
1:12~24, 1:36~48 (24m) 런타임 에러
    본인보다 작은 수가 나왔을 때까지 백트래킹 해서 +1 함
예제) 6
1 2 1 10 4 5
tmp_idx IndexError: list index out of range 발생
dp 출력해보면 [1, 2, 1, 2, 2, 3] 나옴 4가 백트래킹해서 1의 값에 +1 하고 있음. 전의 작은 값들 중에 max 값에다가 +1 해야 됨

~2:14 (26m) 틀렸습니다
틀린 코드
n = int(input())
box = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
for i in range(1, n): 
    if box[i] > box[i-1]:
        dp[i] = dp[i-1] + 1
    else:
        # tmp_idx = i-2
        # while box[i] <= box[tmp_idx] and tmp_idx>=0:
        #     tmp_idx -= 1
        max_prev = -1e8
        for idx, x in enumerate(box[:i]):
            if x < box[i] and dp[idx] > max_prev:
                max_prev = dp[idx] 
        
        if max_prev==-1e8:
            dp[i] = 1 # Reset
        else:
            dp[i] = max_prev + 1
print(max(dp))
TC는 다 맞는데, 어디가 잘못된 걸까? // 다른 풀이로 Solved
'''