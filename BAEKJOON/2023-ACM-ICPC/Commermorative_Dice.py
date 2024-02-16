#20170 - 성공
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

first = list(map(int, input().split()))
second = list(map(int, input().split()))

win_A = 0
for i in first:
    for j in second:
        if i>j:
            win_A += 1

g = gcd(win_A, 36)
print(f'{win_A//g}/{36//g}')