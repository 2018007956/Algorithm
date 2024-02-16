import sys
input = sys.stdin.readline

M = int(input())
S = set([])
for _ in range(M):
    func = input().split()
    if func[0] == 'all':
        S = set([x for x in range(1,21)])
    elif func[0] =='empty':
        S = set([])
    else:
        func, x = func[0], int(func[1]) 
        if func == 'add':
            S.add(x)
        elif func == 'remove':
            S.discard(x)
        elif func == 'check':
            print(1 if x in S else 0)
        elif func == 'toggle':
            S.discard(x) if x in S else S.add(x)
    
        
'''
String으로 함수 호출
locals()[String 변수]()

def a():
    print(0)

param = 'a'
locals()[param]()
-> Class라서 어떻게 적용 시켜야 할지 모르겠음

**  set에서 데이터를 지우는데 'remove'를 사용했는데
이 경우 집합에 지우려는 데이터가 없는 경우 런타임 에러를 띄움
'discard'의 경우 해당 데이터가 없어도 오류가 발생하지 않음

**시간초과**
all에서 i를 문자열로 타입캐스팅 -> int 그대로 사용
=> 성공
'''