# Solved (16m)
import sys
input = sys.stdin.readline
N = int(input())
pattern = input().rstrip().split('*')
for _ in range(N):
    file = input().rstrip()
    
    if len(pattern[0])+len(pattern[1]) <= len(file) and pattern[0] == file[:len(pattern[0])] and pattern[1] == file[-len(pattern[1]):]:
        print('DA')
    else:
        print('NE')
'''
8:14~19 (5m) 69% 틀렸습니다
반례
1
aaa8a
aaa
[정답] NE

~30 (11m)
'''