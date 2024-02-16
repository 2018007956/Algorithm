import sys
input = sys.stdin.readline

class stack:
    def __init__(self): 
        self.items = []
        self.log = []

    def push(self, item): 
        self.items.append(item)
        self.log.append('+')

    def pop(self):  
        self.log.append('-')
        return self.items.pop()

    def peek(self): 
        return self.items[-1]

    def isEmpty(self): 
        return not self.items

    def items_to_list(self):
        return list(self.items)
        
n = int(input())
stk = stack()
x = 1
no = False
for _ in range(n):
    i = int(input())
    while x <= i:
        stk.push(x)
        x += 1

    if not stk.isEmpty() and stk.peek() == i:
        stk.pop()
    else:
        no = True

if no:
    print('NO')
else:
    for i in stk.log:
        print(i)

'''
**시간초과**
끝까지 입력받고 처리 -> 하나 입력받고 바로바로 처리로 바꿈
x in a: x값이 list a에 있는지 확인하는 연산 -> a를 전체 탐색 해야하므로 시간 복잡도 n
    -> NO를 stk.log list에 넣고 확인하지 않고 변수 하나 만들어 체크
    -> while i not in stk.items_to_list() 이 부분도 숫자 비교로 바꿈
'''