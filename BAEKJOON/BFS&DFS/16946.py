# Solved (1h 35m)
import sys
from collections import deque
input = sys.stdin.readline
move = [(0,1), (0,-1), (-1,0), (1,0)]
def bfs(y, x, numbering):
    queue = deque([(x, y)])
    visited[y][x] = True
    cnt = 1
    jido[y][x] = numbering
    while queue:
        x, y = queue.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=ny<N and 0<=nx<M and jido[ny][nx]==0 and not visited[ny][nx]:
                visited[ny][nx] = True
                cnt += 1
                jido[ny][nx] = numbering
                queue.append((nx, ny))

    return cnt

# input
N, M = map(int, input().split())
jido = [list(map(int, input().rstrip())) for _ in range(N)]

# zero grouping
zero_grouping = {}
visited = [[False] * M for _ in range(N)]
num = 2
for i in range(N):
    for j in range(M):
        if jido[i][j]==0 and not visited[i][j]:
            cnt = bfs(i, j, num)
            zero_grouping[num] = cnt
            num += 1

# count the number of grids can be moved
can_move = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if jido[i][j]==1:
            can_move[i][j] = 1
            # checked = [False] * len(zero_grouping)
            checked = set()
            for dx, dy in move:
                nx = j + dx
                ny = i + dy
                if 0<=ny<N and 0<=nx<M and jido[ny][nx]!=1:# and not checked[jido[ny][nx]-2]:
                    # cnt += zero_grouping[jido[ny][nx]]
                    # checked[jido[ny][nx]-2] = True
                    checked.add(jido[ny][nx])
            
            # can_move[i][j] = cnt % 10
            for x in checked:
                can_move[i][j] += zero_grouping[x]
                can_move[i][j] %= 10

for c in can_move:
    print(''.join(map(str,c)))

'''
10:19~36 (15m) 문제 이해
    예제 2의 출력이 이해되지 않음 - 주위 0의 개수!

~ 11:26 (50m) 시간 초과
    문제1 : 특정 0 이 bfs에서 탐색이 안됨 
    원인 : bfs 호출할 때는 (y, x) 로 넣어주고 받을 땐 (x, y)로 생각함
    해결 : def bfs(y, x, ...) 로 수정

    시간 초과
        같은 그룹에 속했는지 확인하기 위해 checked 배열로 방문 여부를 확인하는 것 대신
        set을 만들어서 상하좌우 돌면서 값을 넣고, 그 값들을 더해주는 방식으로 구현
    => 두 방식 시간복잡도 비교 (by GPT)
        1. checked 배열 사용
            N * M 크기의 배열을 순회: O(N * M)
            각 셀에서 4방향 탐색: O(1)
            checked 배열 초기화: O(len(zero_grouping)) (즉, O(max 그룹 수))  -> 새로 알게된 부분 : 배열 크기가 너무 크다면 배열 초기화에도 시간이 걸린다!
            checked 배열 체크 및 업데이트: O(1) (인덱스 접근)
            총 시간 복잡도: O(N * M) + O(N * M * len(zero_grouping))
        2. set 사용
            N * M 크기의 배열을 순회: O(N * M)
            각 셀에서 4방향 탐색: O(1)
            checked에 그룹 번호 추가: O(1) (평균적으로 set의 삽입 및 조회는 O(1))
            checked의 모든 요소에 대해 zero_grouping[x] 합산: 최악의 경우 O(4) (모든 방향에서 고유한 그룹이 나올 경우)
            총 시간 복잡도: O(N * M) + O(N * M * 4) = O(N * M)

~42 (16m) 틀렸습니다
    ** zero_grouping의 값 전체를 더하고 나서 마지막에 % 10을 적용해야 한다 **
    ex) 38 + 25 = 63 -> 63 % 10 (마지막 자리수만 남기기) = 3
        38%10 + 25%10 = 8+5 = 13

~56 (14m) Solved
'''