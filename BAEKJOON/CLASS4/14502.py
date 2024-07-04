# Solved (38m) 
from itertools import combinations
from collections import deque
from itertools import chain
import sys
input = sys.stdin.readline

move = [(0,1), (0,-1), (-1,0), (1,0)]
def spread_virus(start):
    queue = deque(start)
    while queue:
        x, y = queue.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and board[nx][ny]==0:
                board[nx][ny] = 2
                queue.append((nx,ny))


N, M = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
zero_position = [(x,y) for x in range(N) for y in range(M) if jido[x][y]==0]
start_position = [(x,y) for x in range(N) for y in range(M) if jido[x][y]==2]
make_wall = list(combinations(zero_position, 3))

max_safe_area = 0
for case in make_wall:
    board = [item[:] for item in jido] #copy.deepcopy(jido)는 slicing에 비해 많이 느림
    for i, j in case:
        board[i][j] = 1
    
    # 2가 있는 곳 찾아서 퍼져나가기
    spread_virus(start_position)

    safe_area = len([x for x in chain(*board) if x==0])
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)

'''
3개의 벽을 어떻게 선택해야할지 어려웠는데
연구소의 최대 크기가 크지 않으므로 모든 경우의 수를 조합으로 고려해줘도 되었다
    3 ≤ N, M ≤ 8 이므로 둘 다 최대 8이라고 하면, 빈칸의 개수가 최대 63 (64-1 : virus)
    63C3 = 63*62*31/3*2 = 39711


[두 코드 성능 비교]
1. len([x for x in chain(*board) if x==0])
    chain(*board) : 평평한 리스트 만들기 O(N*M)
    리스트 순회하며 조건에 맞는 값 넣기 : O(N*M)
    len : O(1)
    => O(N*M)
2. sum(row.count(0) for row in board)
    각 행에서 0 개수 세기 : O(M)
    각 행의 0 개수 더하기 : O(N)
    => O(N*M)
두 코드의 시간 복잡도는 같음
다만 첫 번째 방법은 chain으로 새로운 iterator를 생성하고, list comprehension으로 추가 리스트를 생성하므로 메모리 할당 면에서 더 비용이 듦
'''