# 1) DFS
def solution(numbers, target):
    cnt = 0
    
    def dfs(idx, cur_sum):
        nonlocal cnt
        if idx == len(numbers):
            if cur_sum == target:
                cnt += 1
            return
    
        dfs(idx+1, cur_sum + numbers[idx])
        dfs(idx+1, cur_sum - numbers[idx])
    
    dfs(0, 0)
    return cnt
'''
nonlocal : 중첩된 함수(내부 함수)에서 바깥 변수를 참조하거나 수정할 때 사용
'''

# 2) 
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
'''
product : 두 개 이상의 리스트의 모든 조합 구함
'''

