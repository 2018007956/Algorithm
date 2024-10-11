# Solved (5m)
def is_good(s):
    stack = []
    for x in s:
        if stack and stack[-1]==x:
            stack.pop()
        else:
            stack.append(x)
    
    if len(stack)==0:
        return True
    else:
        return False

N = int(input())
cnt = 0
for _ in range(N):
    s = input()
    if is_good(s):
        cnt += 1
print(cnt)