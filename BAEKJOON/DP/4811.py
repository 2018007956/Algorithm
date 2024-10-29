# Solved (33m) w/ Search
def dfs(H, W):
    if H < 0 or W < 0:
        return 0
    if H==0 and W==0:
        return 1
    if (H, W) in dp:
        return dp[(H, W)]

    cnt = 0
    # W가 나오는 경우
    cnt += dfs(H+1, W-1)

    # H가 나오는 경우
    cnt += dfs(H-1, W)

    dp[(H, W)] = cnt
    return cnt


while True:
    N = int(input())
    if N==0:
        break
    
    dp = {}
    result = dfs(1, N-1) # 첫번째는 항상 W
    print(result)
'''
9:09~29 (20m) dfs 사용해서 풀었는데 어디가 잘못된지 모르겠다
    종료조건 depth가 아님
    그 단계에서의 값을 구해서 dp에 저장 후 리턴

~42 (13m) Solved
'''