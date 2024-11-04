# Solved (40m)
import sys
input = sys.stdin.readline
def dfs(depth, p, f, s, v, c):
    global min_pay, number, res
    if p>=mp and f>=mf and s>=ms and v>=mv:
        if c < min_pay: # <= 아니라 < 하면 사전 순으로 빠른 게 res에 담김
            min_pay = c
            res = number[:] # 꼭 copy를 해줘야 함. 리스트의 참조를 복사하게 되면 pop 때문에 빈 리스트 출력됨
        return
    if depth >= N or c >= min_pay:
        return

    # 재료를 선택 하는 경우
    cur = nutrients[depth]
    number.append(depth+1)
    dfs(depth+1, p+cur[0], f+cur[1], s+cur[2], v+cur[3], c+cur[4])
    number.pop()
    # 재료를 선택하지 않는 경우
    dfs(depth+1, p, f, s, v, c)


N = int(input())
mp, mf, ms, mv = map(int, input().split())
nutrients = [list(map(int, input().split())) for _ in range(N)]
min_pay = 1e9
number = []
dfs(0, 0, 0, 0, 0, 0)
if min_pay != 1e9:
    print(min_pay)
    print(*res)
else:
    print(-1)
'''
11:48~25 (37m) 50% 넘게 올라가다가 틀렸습니다
    min_pay 업데이트 조건을 if depth==N and [기준값]:으로 했는데, 꼭 depth==N: 가 아니어도 됨
    이 조건 제거해주니 Solved
    그리고 가지치기 조건으로 c>=min_pay도 추가함
'''