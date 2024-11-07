# 알고리즘 공부
import sys
input = sys.stdin.readline
def bellman(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            cur_n, adj_n, w = edges[j]
            # 시작 노드로부터 아직 도달할 수 없는 노드에서의 업데이트를 방지
            if dist[cur_n] != 1e9 and dist[cur_n] + w <dist[adj_n]:
                dist[adj_n] = dist[cur_n] + w
                # N번째에도 업데이트 된다면 음수 사이클 존재
                if i == N-1:
                    return True
    return False


N, M = map(int, input().split())

edges = []
dist = [1e9] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

negative_cycle = bellman(1)
if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == 1e9:
            print(-1)
        else:
            print(dist[i])