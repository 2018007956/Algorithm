# Solved (2h 5m) / 풀이 참고
import sys
from collections import deque
input = sys.stdin.readline
move = [(0,1), (0,-1), (-1,0), (1,0)]
def bfs(x, y):
    queue = deque([(x, y, 0, 1)])
    visited[y][x][0] = 1
    while queue:
        x, y, break_num, time = queue.popleft()
        if (x, y)==(M-1, N-1):
            return time
        
        daytime = time % 2
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=ny<N and 0<=nx<M:
                if jido[ny][nx]=='1' and break_num<K and not visited[ny][nx][break_num+1]:
                    if daytime: # 낮에만 벽을 부술 수 있음
                        visited[ny][nx][break_num+1] = time+1
                        queue.append((nx, ny, break_num+1, time+1))
                    else: # 이동하지 않고 같은 칸에 머물러 있는 경우도 카운트
                        queue.append((x, y, break_num, time+1)) 

                if jido[ny][nx]=='0' and not visited[ny][nx][break_num]:
                    visited[ny][nx][break_num] = time+1 
                    queue.append((nx, ny, break_num, time+1))

    return -1


N, M, K = map(int, input().split())
jido = [input() for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
print(bfs(0, 0))

'''
1:02~19 (17m) 예제 4에서 출력이 11이 나옴
    jido==1 일 때 not visited[ny][nx][break_num+1] 넣어줬었는데 이 조건 없애고 -> 이걸 넣으면 왜 안되는 걸까?
    전체 조건문에 not visited[ny][nx][break_num] 넣으니까 해결

1:31~2:50 (1h 19m) python 시간 초과 pypy 메모리 초과
    다른 풀이 참고 Ref) https://hyundoil.tistory.com/37
    ** 거리정보가 곧 낮/밤 정보 **

3:30~49 (19m) python 1% 시간 초과 pypy 2%? 틀렸습니다
[반례] (https://www.acmicpc.net/board/view/144578)
7 5 1
00000
11110
00000
01111
00000
11111
11110
[정답] 19
[출력] -1

=> if jido==0 일 때 not visited[ny][nx][break_num-1] 조건 제거
    이 조건이 있으면 안되는 이유
        다른 경로에서 벽이 존재하여 부수고 이동한 경우, 그 경로는 폐쇠됨
        벽 안부수고 돌아가는 경로가 측정이 안될 확률 높음

~3:59 (10m) Solved

~5:34 이해가 안되는 부분이 있어 질문 남김
    1. time을 queue에 추가하는 방식으로 메모리 개선이 어떻게 되었는지 
        https://www.acmicpc.net/board/view/147298
    2. 내가 처음 구현했던 time = not time 토글 방식은 왜 안되는지
        https://www.acmicpc.net/board/view/147307
'''