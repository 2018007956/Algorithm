# Solved (32m)
N = int(input())
if N==1:
    print(1)
elif N==2:
    print(2)
else:
    prev2, prev1 = 1, 2
    for i in range(3, N+1):
        cur = (prev2 + prev1) % 15746
        prev2, prev1 = prev1, cur
    print(cur)

'''
N=1: 1 
N=2: 2 
N=3: 3 
N=4: 5 
1:23~27, 4:04~16, 5:48~55 (23m) 메모리초과
    https://www.acmicpc.net/board/view/99300 
    이것도 리스트를 쓴게 문제가 아니라 표현하는 수의 크기가 커져서 메모리 초과가 발생한 것이었음
~58 (3m) 리스트를 변수로 바꿈, 시간 초과
6:07~13 (6m)  숫자가 커지면 메모리를 먹고 덧셈도 오래 걸림 -> 연산 과정에서 나누기 수행
    https://www.acmicpc.net/board/view/141576
'''