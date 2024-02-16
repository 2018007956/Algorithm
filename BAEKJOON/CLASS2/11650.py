import sys
N = int(input())

lst = []
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort()
for i in lst:
    print(i[0], i[1])