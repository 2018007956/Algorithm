# 풀이 공부
import sys
input = sys.stdin.readline
# 북, 동, 남, 서 (시계방향)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def bfs(r, c, d):
    visited[r][c] = True
    cnt = 1
    while True:
        flag = 0
        for _ in range(4):
            d = (d+3) % 4
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and room[nr][nc]==0 and not visited[nr][nc]:
                visited[nr][nc] = True
                cnt += 1
                r = nr
                c = nc
                flag = 1
                break
        
        if flag == 0:
            if room[r-dr[d]][c-dc[d]] == 1:
                print(cnt)
                break
            else:
                r, c = r-dr[d], c-dc[d]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
bfs(r, c, d)
'''
11:36~12:15, 10:07~21 (53m)
이 문제에서 까다로운건 '현재 바라보고 있는 방향'을 고려해줘야 한다는 점인듯
아닌가 어차피 주변 빈칸 다 청소하게 되어있으면 신경안쓰고 동서남북 돌아도될듯
    => 그러면 예제 2번에서 연결된 빈칸이 59개니깐 59가 나와야 하는데 57
    현재 방향 고려해줘야 할듯

    풀이 공부

Point>
왼쪽 방향 회전 : (d+3)%4
    0, 1, 2, 3 => 3, 0, 1, 2
후진 : arr[r-dr[d]][c-dc[d]] 현재 바라보는 방향을 빼준 값 
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
'''