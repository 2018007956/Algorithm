# Solved (43m)
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [1e9] * (N+1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, cur = heapq.heappop(queue)
        if dist > distance[cur]:
            continue

        for adj_n, adj_w in graph[cur]:
            if dist + adj_w < distance[adj_n]:
                distance[adj_n] = dist + adj_w
                heapq.heappush(queue, (distance[adj_n], adj_n))

    return distance


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

# 1) 1->v1->v2->N
result1 = dijkstra(1)[v1]
result1 += dijkstra(v1)[v2]
result1 += dijkstra(v2)[N]

# 2) 1->v2->v1->N
result2 = dijkstra(1)[v2]
result2 += dijkstra(v2)[v1]
result2 += dijkstra(v1)[N]

result = min(result1, result2)
print(-1 if result >= 1e9 else result)

'''
8:13~31 (18m) 틀렸습니다
    1->v1->v2->v1->N, 1->v2->v1->v2->N 도 추가 고려해줘야 하나?
        => 아님. 이미 1->v2 의 최소 경로를 고려해주고 있기 때문에 1->v1->v2 로 한번 더 건너가는 것은 최소 경로가 아님
    양방향 고려

~53 (22m) 퍼센트 엄청 올라가다가 틀렸습니다
    반례) v1, v2 가 1, N이면서 1 -> N으로 가는 경로가 없는 경우
    2 0
    1 2
    [출력] 1e9
    [정답] -1
    마지막 result 조건에서 1e9 보다 크거나 같다로 수정

~56 (3m) Solved
'''