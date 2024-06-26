# 풀이 공부
'''
원래 내 코드에서 수정된 부분
1. 방문 처리: visited 배열을 추가하여 각 칸의 방문 여부를 추적합니다.
2. 사다리 및 뱀 딕셔너리: 사다리와 뱀을 딕셔너리로 관리하여 간단하게 처리합니다.
3. 주사위 눈 처리: 1부터 6까지 모든 경우를 검사하여 다음 칸을 결정합니다.
4. BFS 큐 처리: 각 이동 시 방문 횟수를 함께 저장하여 큐에 추가합니다.
'''
from collections import deque

def bfs():
    queue = deque([(1, 0)])  # (현재 위치, 이동 횟수)
    visited = [False] * 101  # 각 위치의 방문 여부 확인 (1 ~ 100)
    visited[1] = True
    
    while queue:
        x, cnt = queue.popleft()
        
        if x == 100:  # 100번 칸에 도달하면 현재 이동 횟수 출력
            print(cnt)
            return
        
        for i in range(1, 7):  # 주사위 눈 1 ~ 6
            nx = x + i
            if nx > 100:
                continue
            
            # 사다리나 뱀 처리
            if nx in ladders:
                nx = ladders[nx]
            elif nx in snakes:
                nx = snakes[nx]
            
            if not visited[nx]:
                visited[nx] = True
                queue.append((nx, cnt + 1))


N, M = map(int, input().split())
ladders = {}
snakes = {}

for _ in range(N):
    a, b = map(int, input().split())
    ladders[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    snakes[a] = b

bfs()

'''
원래 내 코드 (틀림) 3:55~4:42, 5:45~6:17 22~39 (1h 36m) 

from collections import deque
def bfs():
    queue = deque([1])
    cnt = 0
    while queue:
        x = queue.popleft()
        # print('--',x, cnt)
        for dx in ladder:
            if x==dx[0]:
                nx = dx[1] # 사다리타기
                break
            elif abs(x-dx[0])<=6:
                nx = x + abs(x-dx[0])
            else:
                nx = x + 6            
        else:
            cnt += 1
                
        if not nx in list(zip(*snake))[0]:
            if 0<nx<100: ####
                queue.append(nx)
            else: # nx >= 100
                print(cnt)
                return
                               
N, M = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(N)]
ladder.sort(key=lambda x:x[1])
snake = [list(map(int, input().split())) for _ in range(M)]
snake.sort(key=lambda x:-x[1])
bfs()


틀린 이유 (by GPT)
1. 사다리 및 뱀 처리 로직의 문제
현재 코드에서는 각 칸에 대해 사다리를 먼저 검사한 후, 뱀을 검사합니다. 하지만, 이 검사 방식이 부정확합니다. 
사다리나 뱀에 걸렸을 때 이동할 칸을 결정하는 로직이 복잡하게 되어 있습니다.
사다리와 뱀은 각각 딕셔너리로 처리하는 것이 더 간단하고 직관적입니다.

2.BFS 탐색 로직의 문제
BFS 탐색에서 각 칸을 방문할 때마다 새로운 큐에 추가하는 로직이 일관되지 않습니다. <각 칸에서 가능한 모든 다음 칸을 검사>해야 합니다.
현재 코드는 이동한 후의 칸을 일관되게 큐에 추가하지 않습니다. 그리고 nx 변수의 범위 검사가 잘못되어 있습니다. 100을 포함하지 않도록 해야 합니다.

3.사다리와 뱀을 한 번에 처리하지 않음
현재 코드는 각 칸에 대해 사다리 또는 뱀만 처리하지만, 동시에 처리해야 합니다.
'''