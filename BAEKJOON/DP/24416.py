# Solved (13m)

# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

def fibonacci(n):
    global cnt
    f[1]=f[2]=1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        cnt += 1
    return f[n]

n = int(input())
f = [0] * (n+1)
cnt = 0
print(fibonacci(n), cnt)

'''
12:03~12:11 (8m) 14% 시가초과
코드1의 실행 횟수를 직접 실행하지 않고 계산을 해야함
재귀함수에서 반환한 1이 모여서 해당 피보나치 수가 되기 때문에 코드 1의 실행횟수는 결국 피보나치 수의 값과 동일하다
~16 (5m) Solved
'''