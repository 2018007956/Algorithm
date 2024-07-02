# Solved (46m)
infix = input()

stack = []
postfix = ''
for x in infix:
    if x=='+' or x=='-':
        while stack and stack[-1]!='(':
            postfix += stack.pop()
        stack.append(x)
    elif x=='*' or x=='/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            postfix += stack.pop()
        stack.append(x)
    elif x=='(':
        stack.append(x)
    elif x==')':
        while stack and stack[-1]!='(':
            postfix += stack.pop()
        stack.pop()
    else:
        postfix += x

while stack:
    postfix += stack.pop()
print(postfix)