# Greatest Common Divisor
# x와y의 최대공약수는 y와 x%y의 최대공약수
def gcd(x, y):
    while y>0:
        x, y = y, x%y
    return x
# Least Common Multiple
# x,y의 곱을 a,b의 최대 공약수로 나눈 값
def lcm(x, y):
    return x*y // gcd(x,y)

a, b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))