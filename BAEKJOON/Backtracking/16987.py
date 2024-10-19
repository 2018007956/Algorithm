# Solved (48m) w/ Search
def dfs(depth, x):
    global crash
    if depth==N:
        crash = max(crash, x)
        return

    cur = eggs[depth]
    if cur[0] <= 0:
        dfs(depth+1, x)
        return

    is_hit = False
    for idx in range(N):
        if idx!=depth:
            # 계란치기
            if eggs[idx][0] > 0:
                is_hit = True
                cur[0] -= eggs[idx][1]
                eggs[idx][0] -= cur[1]
            
                cnt = x
                if cur[0] <= 0:
                    cnt += 1
                if eggs[idx][0] <= 0:
                    cnt += 1
                dfs(depth+1, cnt)

                cur[0] += eggs[idx][1]
                eggs[idx][0] += cur[1]

    if not is_hit:
        dfs(depth+1, x)


N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
crash = 0
dfs(0, 0)
print(crash)
'''
11:35~07 GPT Chance!
    **계란이 이미 깨진 경우 처리**
    **계란을 칠 수 없는 경우 처리 (is_hit)**

    몇몇 예제의 실행 시간이 너무 오래걸려서 코드를 다음과 같이 수정했지만 시간 변화 없음
    수정 전
    if cur[0] <= 0 and eggs[idx][0] <= 0:
        dfs(depth+1, x+2)
    elif cur[0] <= 0 or eggs[idx][0] <= 0:
        dfs(depth+1, x+1)
    else:
        dfs(depth+1, x)
    수정 후
    cnt = x
    if cur[0] <= 0:
        cnt += 1
    if eggs[idx][0] <= 0:
        cnt += 1
    dfs(depth+1, cnt)

~23 (48m) Solved
'''