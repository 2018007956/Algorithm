import sys
input = sys.stdin.readline

n = int(input())
dp = [9,9,90,90]

if len(str(n))>4:
    while len(dp)<len(str(n)):
        dp.append(10*dp[len(dp)-2])
# print(dp)

result = sum(dp[:len(str(n))-1]) # 5자리면 4자리:[3]까지 dp 숫자 합함
# print(result)

test = int(str(1)+str(0)*(len(str(n))-2)+str(1)) #네자리면 1001
# print(test)

for i in range(test, n+1):
    x1, x2 = 0, len(str(n))-1
    while True:
        if x1<=x2 and str(i)[x1]==str(i)[x2]:
            x1 += 1
            x2 -=1
            if x1==x2 or x1>x2:
                result += 1
                break
        else:
            break
print(result)