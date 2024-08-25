# 1:20~2:10, 어렵ㄷr
from collections import deque

def bfs():
    queue = deque([(N, 0)])  # (현재 위치, 시간)
    visited[N][0] = 0 
    
    while queue:
        x, t = queue.popleft()
        
        bro_position = K + t * (t + 1) // 2
        if bro_position > 500000:
            print(-1)
            return

        if x == bro_position:
            print(t)
            return

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 500000:
                visited[nx][(t + 1) % 2] = t + 1
                queue.append((nx, t + 1))
                
    print(-1) 

N, K = map(int, input().split())
visited = [[-1] * 2 for _ in range(500001)]  # 시간에 따라 방문 여부 체크
bfs()


# from collections import deque
# def bfs():
#     queue = deque([(N, K)])
#     visited[N] = 0
    
#     while queue:
#         x, k = queue.popleft()
#         if k > 500000:
#             print(-1)
#             break
#         print(x, k)

#         if x == k:
#             print(visited[x])
#             break

#         for i in [x*2, x+1, x-1]:
#             if 0<=i<=500000:
#                 visited[i] = visited[x] + 1
#                 queue.append((i, k+visited[i]))
        
#     else:
#         print(-1)
        

# N, K = map(int, input().split())
# visited = [-1] * (500001)
# bfs()

'''
1:30~2:46 
    예제 6이 무한 루프 걸림. -> 조건문에 not visited 만 넣으면 해결되는데, 그러면 예제2가 답을 못찾아서 무한루프 빠짐
    => 동생이 이동하기 때문에 그 순간의 동생의 위치로 가는 최단경로는 매번 바뀜
    => 이전에 방문했던 곳이라도 최단 경로가 될 여지가 남아있음
    - GPT 찬스 써서 visited 를 홀/짝 구분하여 해야한다는 것을 알게됨 ( 이해.필요)
    
~3:02 python 2% 시간초과 pypy 2% 메모리초과
    방문 조건을 풀고 접근하면 시간 초과 (https://ojt90902.tistory.com/740)

    다음에 다시 도전
'''