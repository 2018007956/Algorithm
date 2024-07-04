# Skills
1. [파이썬 리스트 회전하기](#파이썬-리스트-회전하기)
2. [가중치 트리에서 가장 긴 경로 구하기](#가중치-트리에서-가장-긴-경로-구하기)
3. [2중 리스트 flatten](#2중-리스트-flatten)

## 파이썬 리스트 회전하기
```
k = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# 시계 방향 회전
li = [list(k[::-1]) for k in zip(*k)]
# zip를 써서 각 인덱스의 모든 element를 한 iterator에 넣고 asterisk를 이용하여 풀어서 회전 알고리즘을 구현
# ex) k = [[1, 2, 3],     ->   원하는 출력 form: [[7, 4, 1],
#          [4, 5, 6],                          [8, 5, 2],
#          [7, 8, 9]]                          [9, 6, 3]]
# zip(*k) = [[1, 4, 7],
#            [2, 5, 8],
#            [3, 6, 9]]
print(li)

# 반 시계 방향 회전
li = [list(k) for k in reversed(tuple(zip(*k)))]
# 시계 방향과 동일한 방식이지만, reversed 키워드를 사용하여 배열의 역순 탐색이 가능하게 함
# ex) k = [[1, 2, 3],     ->   원하는 출력 form: [[3, 6, 9],
#          [4, 5, 6],                          [2, 5, 8],
#          [7, 8, 9]]                          [1, 4, 7]]
# reversed(tuple(zip(*k))) = [[3, 6, 9],
#                             [2, 5, 8],
#                             [1, 4, 7]]
print(li)
```

## 가중치 트리에서 가장 긴 경로 구하기
1. 임의의 한 노드에서 가장 먼 노드를 찾고
2. 그 노드에서 다시 가장 먼 노드를 찾는다  

두 번째 구한 거리가 트리에서 가장 긴 경로가 된다.  
문제 : [백준 1967번 트리의 지름](https://github.com/2018007956/Algorithm/blob/master/BAEKJOON/CLASS4/1967.py)

## 2중 리스트 flatten
```
from itertools import chain
list_of_lists = [[x, 0] for x in range(10000)]

%timeit list(chain(*list_of_lists))
# 1000 loops, best of 3: 491 µs per loop

%timeit list(chain.from_iterable(list_of_lists))
# 1000 loops, best of 3: 429 µs per loop
    
%timeit [y for x in list_of_lists for y in x]
# 1000 loops, best of 3: 725 µs per loop
    
%timeit sum(list_of_lists, [])
# 1 loop, best of 3: 211 ms per loop

참고 : https://www.winterjung.dev/list-of-lists-to-flatten/
```