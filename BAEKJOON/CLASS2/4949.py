while True:
    stack = []

    s = input()
    if s == '.':
        break

    for i in s:
        if i == '(' or i =='[':
            stack.append(i)
        elif i == ']':
            if len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            else:
                print('no')
                break
        elif i == ')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                print('no')
                break
    else:
        if len(stack)==0:
            print('yes')
        else:
            print('no') # 열린 괄호가 남음

    


'''
마지막조건: 괄호 사이에 있는 문자열도 균형이 잡혀야 한다 - 이게 무슨 말?

한 가지 빼먹고 생각해서 틀림
열린 괄호가 닫힌 괄호보다 많이 등장하는 경우 yes로 출력될 수 있음 
-> 마지막에 len 확인
'''