# Solved (32m)
import sys
input = sys.stdin.readline
N, X = map(int, input().split())
visitor = list(map(int, input().split()))

sum_visit = sum(visitor[:X])
max_visit = sum_visit
cnt = 1
for i in range(X, N):
    sum_visit = sum_visit - visitor[i-X] + visitor[i]
    if sum_visit > max_visit:
        max_visit = sum_visit
        cnt = 1
    elif sum_visit == max_visit:
        cnt += 1
        
if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(cnt)
'''
10:22~35 (13m) 시간 초과
    윈도우의 합을 한 번 구한 후, 윈도우를 이동하면서 추가 계산

~46 (9m) 64%쯤 틀렸습니다
    cnt가 출력되는 경우에는 반복문을 돌면서 cnt가 항상 업데이트 될것이라 착각하여 아무값 0으로 초기화함
    제일 첫 sum_visit이 max_visit이 될 수 있기에 cnt=1로 정의 필요

~56 (10m) Solved
'''