# Solved
def solution(tickets):
    answer = []
    tickets.sort()
    
    def dfs(path):
        if len(path)==len(tickets)+1:
            answer.append(path)
            return
        
        for i, (s, e) in enumerate(tickets):
            if not visited[i] and path[-1]==s:
                visited[i] = True
                dfs(path+[e])
                visited[i] = False
    
    visited = [False] * len(tickets)
    dfs(["ICN"])
    return answer[0] # 사전순이므로 첫 번째 리턴
'''
visited = set() 으로 목적지 e만 방문 체크 
→ 같은 목적지로 가는 여러 티켓 구분 안 됨 → 티켓 중복 사용 방지 실패
'''

# 다른 사람 풀이 -  Hierholzer's Algorithm
def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            path.append(stack.pop())

    return path[::-1]
'''
dictionary get(찾고자 하는 key값, key가 없을 때 리턴할 default값)

Hierholzer 알고리즘은 오일러 회로(Euler circuit)를 찾는 알고리즘
https://github.com/2018007956/Teamnote-archive/blob/main/Searching/Hierholzer.py
'''