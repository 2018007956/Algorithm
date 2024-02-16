M, N = map(int, input().split())

def is_prime(x):
    if x==1:    return False
    for i in range(2, int(x**0.5)+1):
        if x % i ==0:
            return False
    return True

for i in range(M,N+1):
    if is_prime(i):
        print(i)

'''
그 수까지 검사하면 시간초과 -> 제곱근까지 검사
'''