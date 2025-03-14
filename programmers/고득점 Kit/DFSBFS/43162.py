# Not Solved
# 1) BFS
from collections import deque
def bfs(start, computers):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in range(len(computers)):
            if computers[node][neighbor]==1 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
def solution(n, computers):
    global visited
    answer = 0 
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i, computers)
            answer += 1
    return answer

'''
이동 방향이 아니라, 네트워크 연결 여부(computers[i][j])를 기준으로 BFS/DFS 수행
'''

# 2) DFS
def dfs(node, computers):
    visited[node] = True
    for neighbor in range(len(computers)):
        if computers[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, computers)

def solution(n, computers):
    global visited
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, computers)
            answer += 1
    return answer