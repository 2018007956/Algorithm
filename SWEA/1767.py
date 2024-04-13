# 프로세서 연결하기
# BackTracking / 2h 34m / not solved
file = open('./input.txt', 'r')
def input():
	return file.readline()

def isPower(r, c):
    return r < 0 or r >=N or c <0 or c >= N

def isValid(r, c):
    return processer[r][c]!=1 and not visited[r][c]

def dfs(depth, cnt, connect):
    global answer
    global max_connect
    if depth == len(core):
        if connect > max_connect:
            max_connect = connect
            answer = cnt
        elif connect == max_connect:
            answer = min(answer, cnt)
    #     return cnt # 이렇게 구현하면 안되는 이유 : leaf node에서 cnt를 리턴하지만 그 부모 노등서 None 리턴됨 (ref1)
        return

    for k in range(depth, len(core)):
        r, c = core[k]
        for i in range(4):
            flag = False
            tmp = set()
            next_r, next_c = r, c
            while True:
                next_r += dr[i]
                next_c += dc[i]

                if isPower(next_r, next_c):
                    flag = True
                    break
                if not isValid(next_r, next_c):
                    break
                tmp.add((next_r, next_c))

            # 가능하다면 전선 연결
            if flag:
                leng = 0
                for px, py in tmp:
                    visited[px][py] = True
                    leng += 1
                dfs(k +1, cnt + leng, connect+1)

                for px, py in tmp:
                    visited[px][py] = False

T = input() # # of TestCase
for tc in range(1, int(T)+1):
    answer = 1e8
    max_connect = 0
    N = int(input())
    processer = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    result = 0
    core = []
    for x in range(N):
        for y in range(N):
            if x!=0 and y!=0 and x!=N-1 and y!=N-1 and processer[x][y] == 1:
                core.append((x,y))

    dfs(0, 0, 0)
    print(f'#{tc} {answer}')

'''
code ref : https://door-of-tabris.tistory.com/entry/%EC%82%BC%EC%84%B1sw-1767%EB%B2%88-%ED%94%84%EB%A1%9C%EC%84%B8%EC%84%9C-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0%ED%8C%8C%EC%9D%B4%EC%8D%AC
ref1 : https://velog.io/@munang/%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-Python-None-%EB%A6%AC%ED%84%B4%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0-%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98-None-%EB%A6%AC%ED%84%B4
'''