# Solved (58m)
from collections import deque
def right(num, d):
    if num > 3:
        return
    if topni[num-1][2] != topni[num][-2]:
        right(num+1, -d)
        topni[num].rotate(d)

def left(num, d):
    if num < 0:
        return
    if topni[num][2] != topni[num+1][-2]:
        left(num-1, -d)
        topni[num].rotate(d)


topni = [deque(input()) for _ in range(4)]
K = int(input())
for _ in range(K):
    num, d = map(int, input().split())
    num -= 1

    left(num-1, -d)
    right(num+1, -d)

    topni[num].rotate(d)
                
score = 0
for i, x in enumerate(topni):
    score += int(x[0]) * (2**i)
print(score)

'''
다른 풀이 공부 https://sooz.tistory.com/106 
1. deque().rotate() 함수 안에 양수를 넣으면 오른쪽 방향으로, 음수를 넣으면 왼쪽 방향으로 숫자만큼 회전한다
2. '1번 톱니바퀴는 2번이 회전하지 않았기 때문에, 회전하지 않게 된다.'라는 연쇄 조건은 dfs로 구현
'''