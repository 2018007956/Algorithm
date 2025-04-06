# Solved
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# 다른 사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''
map 함수 기본 문법 : map(function, iterable)
    function : 각 요소에 적용할 함수
    iterable : 함수를 적용할 데이터 집합
'''