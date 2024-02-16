import math
N = int(input())
s = str(math.factorial(N))[::-1]
for i in range(len(s)):
    if s[i]!='0':
        print(i)
        break

'''
끝에서부터 0이 아닌 수를 만날 때까지의 0의 개수를 구하는 법은 x10의 개수이므로 
소인수분해 했을 때 2의 개수와 5의 개수 중 작은 것의 수= x5의 개수
2의 지수가 5의 지수보다 항상 더 큼

N = int(input())
print(N//5 + N//25 + N//125)
'''