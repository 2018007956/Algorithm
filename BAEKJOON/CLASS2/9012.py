from collections import Counter
T = int(input())

for i in range(T):
    data=input()
    stack = []
    chk = 0
    for j in data:
        if j=='(':
            stack.append('(')
        else:
            if len(stack)==0:
                chk = 1
                break
            stack.pop()
    if chk !=1 and len(stack)==0:
        print('YES')
    else:
        print('NO')

'''
stack = [] 안쓰고 
변수로 (: +1, ): -1 하면서
음수가 되면 NO 출력하고 break,
변수가>0: NO, ==0: YES

또 다른 방법)
chk 변수 안쓰고 for-else문 구현
T = int(input())
for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됬을경우 수행한다
        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")
'''