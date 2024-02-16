import sys
from functools import cmp_to_key
N = int(input())

lst = []
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

def sort_func(a,b):
    if a[1] == b[1]:
        if a[0] > b[0]: 
            return 1 # 순서 뒤집기
        else:
            return -1 # 순서 그대로
    else:
        return 0

lst.sort(key = lambda x:x[1])
lst.sort(key = cmp_to_key(sort_func))
for i in lst:
    print(i[0], i[1])


'''
3
2 2
3 2
1 2

cmp_to_key(): custum 조건에 따라 sorting 가능
return 음수: 먼저 들어온 요소가 앞으로 정렬됨
return 0: 바뀌지 않음
return 양수: 나중에 들어온 요소가 앞으로 정렬됨 (먼저 들어온 요소보다 앞에 배치됨)
'''

'''
def sort_func(a,b):
    if a[1] == b[1]:
        if a[0] > b[0]: 
            return 1 # 순서 뒤집기
        else:
            return -1 # 순서 그대로
    return 0
--> 이렇게 하니까 런타임 에러 뜸
'''