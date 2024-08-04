# Solved (20m) w/ 풀이 참고
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
value_board = [[0] * (K+1) for _ in range(N+1)]
for n in range(1, N+1):
    w, v = map(int, input().split())
    for k in range(1, K+1):
        if k < w:
            value_board[n][k] = value_board[n-1][k]
        else:
            value_board[n][k] = max(value_board[n-1][k-w]+v, value_board[n-1][k])

print(value_board[n][k])

'''
9:30~50 (20m) python, pypy 둘 다 1% 시간 초과
    w0, v0 = data[0]
    if w0 <= K:
        dp[0] = (w0, v0)

    for i in range(1, N+1):
        if dp[i-1][0] + data[i][0] <= K:
            dp[i] = dp[i-1][1] + data[i][1]
    ...
    dp는 잘 모르겠음
    조건이 있는 조합 계산 -> 조합 계산해서 조건에 맞게 필터링
    근데 이렇게 풀린다고 해도, 기업 코테에서 이 방식은 시간 초과 반드시 뜰 것 같긴 함
    그래도 안푸는 것 보다야 나으니까.

    조합을 사용한 브루트포스 방식으로 간단하게 풀었지만 역시나 시간초과

Knapsack problem 공부 / 다음에 다시 시도
Ref) https://velog.io/@dmsgur7112/Knapsack%EB%B0%B0%EB%82%AD-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

11:42~12:02 (20m) Solved, but 풀이 참고 / 다음에 한 번 더 풀어볼 필요
'''