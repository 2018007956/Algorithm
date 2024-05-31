# Solved (24m) w/ search
import sys
input = sys.stdin.readline
data = input().rstrip()
bomb = input().rstrip()
stack = []
for char in data:
    stack.append(char)
    if ''.join(stack[-len(bomb):])==bomb:
        del stack[-len(bomb):]
if stack:
    print(''.join(stack))
else:
    print('FRULA')