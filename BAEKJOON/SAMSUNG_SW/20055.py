# Solved (30m) w/ Search - 어렵진 않지만 자잘한 조건들이 많은 문제
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
A = deque(map(int, input().split()))

cnt = 0
robot = deque([False] * N) # n개의 벨트만 로봇이 존재할 수 있음
while True:
    cnt += 1

    # 1. 벨트가 각 칸 뒤에 있는 로봇과 함께 한 칸 회전한다.
    A.rotate(1)
    robot.rotate(1)

    # 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    robot[N-1] = False

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한칸 이동할 수 있다면 이동한다.
    for i in range(N-2, -1, -1):
        # 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        if robot[i] and robot[i+1] == False and A[i+1] >= 1:
            robot[i], robot[i+1] = False, True
            A[i+1] -= 1

    # 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    robot[N-1] = False

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if A[0] != 0:
        robot[0] = True
        A[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
    if A.count(0) >= K:
        break

print(cnt)