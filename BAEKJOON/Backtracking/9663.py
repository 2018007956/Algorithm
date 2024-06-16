# 풀이 공부
n = int(input())
isused1 = [False] * n   # (y) column을 차지하고 있는지
isused2 = [False] * 2*n   # (x+y) / 방향 대각선을 차지하고 있는지
isused3 = [False] * 2*n   # (x-y+n-1) \ 방향 대각선을 차지하고 있는지

cnt = 0
def dfs(cur):
    global cnt
    if cur==n:
        cnt += 1

    for i in range(n):
        if isused1[i] or isused2[i+cur] or isused3[cur-i+n-1]:
            continue
        isused1[i] = True
        isused2[i+cur] = True
        isused3[cur-i+n-1] = True
        dfs(cur+1)
        isused1[i] = False
        isused2[i+cur] = False
        isused3[cur-i+n-1] = False


dfs(0)
print(cnt)

'''
우하향 대각선(\) x-y의 값은 -(n-1)에서 n-1까지이다.
예를 들어, 8x8 체스판에서 (x-y)의 값은 -7에서 7까지이다.
배열 인덱스를 양수로 변환해주기 위해서 x-y에 n-1을 더한다.
n-1을 더해주면 최솟값인 -(n-1)은 0이 되고, 최댓값인 (n-1)은 2*(n-1)이 되어 모든 값이 양수 인덱스 범위로 변환된다.
'''