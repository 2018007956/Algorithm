# Not Solved - 숫자간 규칙 파악
k = int(input())
res = ''
while k > 0:
    n = k % 2 # 홀짝 판별
    k //= 2
    if n == 0:
        k -= 1
        res = '7' + res
    else:
        res = '4' + res

print(res)