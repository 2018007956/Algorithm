# Not Solved
import sys
input = sys.stdin.readline

arr = input()

stack = []
answer = 0
tmp = 1
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
        tmp *= 2

    elif arr[i] == '[':
        stack.append(arr[i])
        tmp *= 3

    elif arr[i] == ')':
        if arr[i-1] == '(':
            answer += tmp
        else:
            answer = 0
            break
        stack.pop()
        tmp //= 2
        
    else:
        if arr[i-1] == '[':
            answer += tmp
        else:
            answer = 0
            break
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)
'''
38%쯤 틀렸습니다
반례 : (((())())())
정답 : 28
출력 : 12
이유 : res에 값이 들어있고, 다시 ( or [ 로 열릴 경우 고려 X

반례2 : ()(())
정답 : 6
출력 : 8

//////
-> stack에 괄호와 숫자를 다 넣으면 타입 체크도 필요하고 복잡,
-> 문자만 넣고 숫자는 변수에 따로 계산
'''