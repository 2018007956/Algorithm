# 풀이 공부
N, K = map(int, input().split())
number = input()

stack = []
for num in number:
    while stack and K > 0 and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)
    
if K > 0:
    stack = stack[:-K]

print(''.join(stack))