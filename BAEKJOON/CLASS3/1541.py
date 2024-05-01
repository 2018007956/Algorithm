# Solved (1h 50m)
exp = input().split('-')

cal = []
for x in exp:
    if '+' in x:
        cal.append(sum(map(int, x.split('+'))))
    else:
        cal.append(int(x))

answer = cal[0]
for i in cal[1:]:
    answer -= i
print(answer)

'''
11:50~12:44 (54m) 런타임 에러 발생

import re

exp = input()
tmp = 0
for idx, x in enumerate(exp):
    if x=='-':
        if tmp%2==0:
            exp = exp[:idx+1]+'('+exp[idx+1:]
        else:
            exp = exp[:idx+1]+')'+exp[idx+1]+'('+exp[idx+2:]
        tmp += 1


changer = re.split('([^0-9])',exp)
for idx, x in enumerate(changer):
    try:
        changer[idx] = str(int(x))
    except:
        pass


exp = ''.join(changer)
try:
    print(eval(exp)) 
except: # 마지막 괄호 안닫힌 경우
    print(eval(exp+')'))

https://ideone.com/iJz2O1 이 사이트를 통해 확인해보니 아래와 같은 에러가 떴다
TypeError: 'int' object is not iterable
-> input().strip()으로 공백 제거해주니 
exp = input().strip()에서 EOFError: EOF when reading a line 에러 발생

런타임 원인 찾으려고 찾아보다가 더 간단한 풀이 방식 알게되어 
풀이 구조 바꿔서 다시 풀었더니 Solved
위 런타임에러 발생 코드는 원인 못찾음
'''