# Solved (15m)
import sys
import math
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for x in A:
    x -= B
    cnt += 1
    if x > 0:
        cnt += math.ceil(x/C)
print(cnt)
'''
만약 B < C 이면 모든 시험장에 부감독관만 넣고 최소수 구하려했더니 예제 4번에서 다른 답이 나옴
각 시험장마다 총감독관은 꼭 한명씩 있어야 하는건가? 싶어서 그렇게 구현해봤더니 예제 모두 정답
    => '각각의 시험장에 총감도관은 오직 1명만 있어야 하고, 부감독관은 여러 명 있어도 된다.'
    이 말이 각 시험장에 총감독관이 1명 꼭 있어야 한다는 말인듯
'''