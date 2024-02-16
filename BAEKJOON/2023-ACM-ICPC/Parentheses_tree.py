#26111
import sys
input = sys.stdin.readline
s = input()

total = 0
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        if s[i+1] == ')':
            total+= cnt
            continue
        cnt += 1
    elif s[i] == ')':
        if s[i-1] == '(': # right parentheses of node, so no decrease
            continue 
        cnt -= 1
print(total)