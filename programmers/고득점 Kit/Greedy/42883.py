# Not Solved
def solution(number, k):
    stack = []
    for x in number:
        while stack and k>0 and stack[-1]<x:
            stack.pop()
            k-=1
        stack.append(x)
        
    if k>0:
        stack = stack[:-k]
    return ''.join(stack)
'''
순서가 고정된 상황 -> 순차적 탐색하고, 뒤에서 앞 상황 고려할 필요 없음
=> "앞자리부터 가능한 한 큰 숫자를 남기자"
'''