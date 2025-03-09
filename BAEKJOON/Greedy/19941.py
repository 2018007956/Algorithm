## 풀이 공부

# 1) Greedy
# 백트래킹(DFS)처럼 모든 경우를 탐색하지 않아도, Greedy 방식은 항상 최적의 배정을 수행할 수 있다.
# 수학적으로, 매칭 문제에서 탐욕법이 최적해를 보장하는 경우는 "각 단계에서 최적의 선택이 전체 최적해를 해치지 않을 때"인데, 이 문제는 이 조건을 만족한다.
N, K = map(int, input().split())
arr = list(input())
visited = [False] * N
result = 0

for i in range(N):
    if arr[i] == 'P':
        for j in range(max(0, i - K), min(N, i + K + 1)):  # K 범위 내에서 햄버거 탐색
            if arr[j] == 'H' and not visited[j]:  # 햄버거를 아직 먹지 않았다면
                visited[j] = True  # 해당 햄버거 먹음 처리
                result += 1
                break  # 한 번만 먹을 수 있으므로 중단

print(result)

# 2) DFS
'''
import sys
sys.setrecursionlimit(100000)
N, K = map(int, input().split())
arr = input()
visited = [False] * N
result = 0

def eatHamburgur(idx, cnt):
    global result
    if idx >= N:
        result = max(result, cnt)
        return

    if arr[idx] == 'P':
        for d in range(-K, K+1):
            h_idx = idx + d
            if 0 <= h_idx < N and not visited[h_idx] and arr[h_idx] == 'H':
                visited[h_idx] = True
                eatHamburgur(idx+1, cnt+1)
                visited[h_idx] = False
                return
            
    eatHamburgur(idx+1, cnt)


eatHamburgur(0,  0)
print(result)
'''

'''
11:10~24 1% 틀렸습니다
~48, 10:00~20 풀이 공부
    햄버거를 먹을 수 있는 최대 사람 수를 구하려면, "가장 가까운 햄버거를 먹도록" 구현
    왼쪽부터 탐색하고 있기 때문에 (가장 가까운 == 가장 왼쪽) 그래야 뒤에 있는 P가 H를 먹을 가능성을 높임
'''