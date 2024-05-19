# Solved (41m)
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1]
    if n!=0: # 빈 리스트([])은 split(',') 안 함
        arr = deque(arr.split(','))

    cnt = 0
    for x in p:
        if x=='R':
            cnt += 1
        else: # D
            if arr:
                if cnt % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                break
    else:
        if cnt % 2 == 1 and arr:
            arr.reverse()
            print('['+','.join(arr)+']')
        else:
            print('['+','.join(arr)+']')
'''
9:43~50, 57~00, 28~35 (17m) 런타임에러

10~30 (20m) 16% 런타임 에러
    출력형태 맞춰주기, 
    reverse 시간복잡도 : O(N) 고려 -> 모든 R을 다 reverse하게 되면 최대 O(len(p)*n)=100,000*100,000=10^10 이므로 시간초과

30~34 (4m) Solved
Ref) https://www.acmicpc.net/board/view/141784
아래 예시 고려 (D가 안들어와서 error는 안뜨는데 비어있는 배열에 접근하는 경우)
1
R
0
[]
if arr 조건 추가해줘서 Solve
'''