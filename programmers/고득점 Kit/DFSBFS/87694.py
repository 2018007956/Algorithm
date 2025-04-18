# Not Solved - Too hard (이해X)
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):

    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    graph = [[-1]*101 for _ in range(101)]
    # 직사각형 내부는 0, 테두리는 1로 표시
    for rec in rectangle:
        a, b, c, d = map(lambda x : x*2, rec) # 좌표를 2배로 확대
        for x in range(a, c+1):
            for y in range(b, d+1):
                if a < x < c and b < y < d:
                    graph[x][y] = 0 # 내부: 완전 차단
                elif graph[x][y] != 0:
                    graph[x][y] = 1 # 테두리: 통과 가능

    # BFS 실행
    ret = 0
    visited = set()
    q = deque()
    q.append((characterX*2, characterY*2, 0))
    visited.add((characterX*2, characterY*2))
    while q:
        x, y, level = q.popleft()
        if x == itemX*2 and y == itemY*2:
            ret = level // 2
            break

        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0 <= nx <= 100 and 0 <= ny <= 100 and not (nx, ny) in visited and graph[nx][ny] == 1:
                q.append((nx, ny, level+1))
                visited.add((nx, ny))

    return ret

'''
[좌표를 2배로 확대하는 이유]
2배 확대를 안 하면, 격자 점만으로는 "내부 vs 테두리" 구분이 불명확해서,
캐릭터가 대각선으로 내부를 가로질러 버릴 수 있음.

2배 확대를 하면, 그래프상에서 내부, 테두리, 외부를 완벽히 구분할 수 있고,
BFS로 "테두리만 따라가는 경로"를 명확하게 탐색할 수 있음.
'''