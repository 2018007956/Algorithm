import sys
input = sys.stdin.readline

N, M = map(int, input().split())
group1 = [input().strip() for _ in range(N)]
group2 = [input().strip() for _ in range(M)]
dup = list(set(group1) & set(group2))
print(len(dup))
for i in sorted(dup):
    print(i)

'''
입력받을때마다 기존에 있는 리스트에 들어있는지 확인하고 있으면 중복된 것으로 출력
-> 시간초과
-> 집합으로 받아서 &로 중복된 부분 출력
-> 출력시 \n 포함되어 출력됨
-> strip() 추가
'''