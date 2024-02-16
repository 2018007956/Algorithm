import sys
input = sys.stdin.readline

cnt0 = 0
cnt1 = 0
def fibonacci(n):
    global cnt0, cnt1
    if n==0:
        cnt0 += 1
        return 0
    elif n==1:
        cnt1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

T = int(input())
for _ in range(T):
    N = int(input())
    fibonacci(N)
    print(cnt0, cnt1)
    cnt0, cnt1 = 0,0

'''
전역변수로 하나씩 카운팅 -> 시간초과

'''