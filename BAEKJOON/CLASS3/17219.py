# solved (9m)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

db = {}
for _ in range(N):
    site, passwd = input().split()
    db[site] = passwd

result = []
for _ in range(M):
    result.append(db[input().strip()])

for i in result:
    print(i)

'''
1 ≤ N ≤ 100,000, 1 ≤ M ≤ 100,000
여러 줄을 입력받거나 출력할 때 시간이 느림 (그래도 시간 제한 5초여서 solve 뜸)
input = sys.stdin.readline 추가했더니 훨씬 빨라진 속도 확인 : 7736ms -> 236ms
'''