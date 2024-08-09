# Solved (1h 47m)
import sys
input = sys.stdin.readline

def go_stack(stack, x):
    try:
        if x[:3] == 'NUM':
            stack.append(int(x.split()[1]))
        if x == 'POP':
            stack.pop()
        if x == 'INV':
            stack[-1] = -stack[-1]
        if x == 'DUP':
            stack.append(stack[-1])
        if x == 'SWP':
            stack[-1], stack[-2] = stack[-2], stack[-1]
        if x == 'ADD':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        if x == 'SUB':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        if x == 'MUL':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        if x == 'DIV':
            a = stack.pop()
            b = stack.pop()
            if a*b < 0:
                stack.append(-(abs(b)//abs(a)))
            else:
                stack.append(abs(b)//abs(a))
        if x == 'MOD':
            a = stack.pop()
            b = stack.pop()
            if b < 0:
                stack.append(-(abs(b)%abs(a)))
            else:
                stack.append(abs(b)%abs(a))

        if stack and abs(stack[-1])>1e9:  
            return "ERROR"
        
        return stack

    except:
        return "ERROR"
    

def execute():
    for num in V:
        # execute program for each input
        stack = [num]
        for x in program:
            # print('x:',x)
            stack = go_stack(stack, x)
            # print('---',stack)
        else:
            if len(stack)!=1 or abs(stack[-1])>1e9:
                print('ERROR')
            else:
                print(stack[0])    


program = []
error = False
while True:

    x = input().rstrip()
    program.append(x)

    if x == 'END':
        N = int(input())
        V = [int(input()) for _ in range(N)]
        execute() 
        print()
        program = []
        error = False

    if x == 'QUIT':
        break

'''
2:36~3:35 (1h) 16 % 런타임 에러
    append 오타

~3:57, 4:30~ 
    try except으로 처리하지 말고 각각의 경우를 직접 에러 처리 해줘야 하나?
    전역변수 error를 다루는 부분에서 문제가 있나? return으로 다루는 방식으로 바꿔봄
    확인해보니 전역변수가 아니라
        abs(stack[-1])>1e9에서 stack이 비어있는 경우도 있을 수 있어서 런타임 에러 발생
        앞에 stack and 조건 추가
        https://www.acmicpc.net/source/82261091 => 그런데 16% 틀렸습니다 뜨는 이유는 모르겠다.

~4:53 (45m) 16% 출력형식이 잘못되었습니다.
    문제 조건 - 각 기계에 대한 출력값을 모두 출력한 뒤에는 빈 줄을 하나 출력해야 한다.
    print() 추가

~4:55 (2m) Solved 
'''