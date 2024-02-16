# Gift Discount
# https://contest.icpckorea.org/domjudge/team/problems/2/text
import sys
input = sys.stdin.readline

n, b, a = map(int, input().split())
price = list(map(int, input().split()))
price.sort()

cal_p = 0
cnt = 0
for i in range(n):
    if cal_p+price[i] <= b:
        cal_p += price[i]
        cnt += 1
    else: # discount
        if cal_p+price[i]/2 <=b and a>0:
            cal_p += price[i]/2
            cnt += 1
            a -= 1

print(cnt)