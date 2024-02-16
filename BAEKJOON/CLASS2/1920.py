N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in B:
    print('1' if i in A else '0')

'''
list A일때는 시간초과
set A로 바꾸니 통과
'''