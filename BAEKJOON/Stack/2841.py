# Solved (30m)
import sys
input = sys.stdin.readline
N, P = map(int, input().split())

cnt = 0
stack = [[] for _ in range(7)]
for _ in range(N):
    line, pret = map(int, input().split())
    
    while stack[line] and stack[line][-1] > pret:
        stack[line].pop()
        cnt += 1

    if stack[line] and stack[line][-1] == pret:
        continue
        
    stack[line].append(pret)
    cnt += 1

print(cnt)
'''
7:15~39 (24m) 런타임에러 (IndexError)
~46 (7m) Solved
    줄 6개인데 index 1부터 사용하기 때문에 7개로 세팅
    
    조건들의 순서를 고려하고 pass가 아닌 continue를 사용하여 코드 개선
'''