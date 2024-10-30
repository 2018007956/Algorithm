# Solved (46m) w/ Search
import sys
input = sys.stdin.readline
N = int(input())
tower = list(map(int, input().split()))

result = []
stack = []
for i in range(N):
    while stack and stack[-1][0] < tower[i]:
        stack.pop()
        
    if stack:
        result.append(stack[-1][1]+1)
    else:
        result.append(0)

    stack.append((tower[i], i))
        
print(*result)
'''
숫자가 커지는 부분을 stack에 저장해놓고 스택의 마지막 값과 현재 값을 비교

9:12~45 (33m) 3% 틀렸습니다
    스택에 값 넣는 조건이 틀린듯
    스택에는 가장 가까운 탑의 정보 유지
    스택의 최상단의 높이가 현재 탑보다 낮으면, 스택에서 제거    

~58 (13m) Solved
'''