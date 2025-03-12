# Solved (47m)
import sys
import heapq
input = sys.stdin.readline
N, centi, T = map(int, input().split())
H = [int(input()) for _ in range(N)]

maxHeap = []
for x in H:
    heapq.heappush(maxHeap, -x)

cnt = 0
for _ in range(T):
    if -maxHeap[0]==1 or -maxHeap[0] < centi:
        break
    heapq.heapreplace(maxHeap, -(-maxHeap[0]//2))
    cnt += 1

if maxHeap and -maxHeap[0] >= centi: #any(x <= -centi for x in maxHeap):
    print('NO', -maxHeap[0], sep='\n')
else:
    print('YES', cnt, sep='\n')

'''
highest//2와 -(highest//2)는 다름
10:20~47 (27m) 2% 틀렸습니다
    maxHeap이라서 - 부호 생각하는 부분에서 실수함
    if highest > centi가 아니라 < 임 센티보다 작은 키가 있으면 멈춰야 함
~56 (10m) 92%? 런타임 에러 (IndexError)
    maxHeap이 안비어있는 경우 접근하도록 조건 추가
~11:09~ (10m) Solved

코드 효율화
    heapq.heapreplace(maxHeap, 7) : 힙에서 가장 작은 원소를 팝한 후 원소 7을 푸시
    최대값을 pop하지 않고 [0] 이렇게 인덱스로 접근
'''