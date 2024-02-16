import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
M = int(input()) # len of S
S = input()

# Print how many Pn in S


# print('OOIOIOIOIIOII'.count('IOI')) -> 3 -> 겹치는게 안세지므로 
# 마지막 자리 빼고 찾고, 그 다음 문자 확인 하는 방법 ?

counter = Counter("OOIOIOIOIIOII")
print(counter)
print(counter["IOI"])