import re
N = int(input())
find_num = []
for _ in range(N):
    find_num.extend(list(map(int, re.findall(r'\d+', input()))))
for x in sorted(find_num):
    print(x)
'''
정규 표현식 패턴
    \d : 0부터 9까지의 모든 숫자
    + : 하나 이상의 문자
'''