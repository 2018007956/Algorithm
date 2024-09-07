# Solved (38m)
import sys
input = sys.stdin.readline
N, H = map(int, input().split())
up = [0] * (H + 1)
down = [0] * (H + 1)

for i in range(N):
    height = int(input())
    if i % 2 == 0:
        # 석순의 시작 지점에 +1
        down[height] += 1
    else:
        # 종유석의 끝 지점에 +1
        up[height] += 1

# 누적합 계산 (Prefix Sum)
for i in range(H-1, 0, -1):
    down[i] += down[i+1]
for i in range(H-1, 0, -1):
    up[i] += up[i+1]

# 최솟값과 그 높이 찾기
min_obstacles = float('inf')
count = 0
for i in range(1, H + 1):
    obstacles = down[i] + up[H-i+1]
    if obstacles < min_obstacles:
        min_obstacles = obstacles
        count = 1
    elif obstacles == min_obstacles:
        count += 1

print(min_obstacles, count)
'''
cumulate = [0] * H
for i in range(N):
    if i%2==0:
        for x in range(hurdle[i]):
            cumulate[x] += 1
    else:
        for x in range(hurdle[i]):
            cumulate[H-1-x] += 1

위와 같이 구현하면 시간 복잡도가 O(200,000 * 500,000) = O(100,000,000,000)라서 무조건 시간 초과 발생
어떻게 개선할 수 있을까?
2:44~06 (22m)
    어떻게 개선해야 할지 모르겠다. 역시나 pypy 4% 시간초과
    GPT Hint) 각 장애물의 높이 범위에 대해 반복문을 돌리면서 누적합을 계산하는 대신 
    각 높이에서 장애물이 시작되고 끝나는 지점을 기록하고 이를 바탕으로 *뒤에서부터* 누적합을 계산하는 방법을 사용

9:28~44 (16m) Solved
'''