# Not Solved
from collections import deque
def bfs(x):
    cnt = 0
    queue = deque([(x, cnt)])
    visited = set()
    while queue:
        x, cnt = queue.popleft()
        cnt += 1
        for y in range(1, int(x**(1/2))+1):
            nx = x - y*y
            if nx == 0:
                return cnt
            if nx not in visited:
                visited.add(nx)
                queue.append((nx, cnt))
            
n = int(input())
print(bfs(n))
# 46% 쯤 시간초과, PyPy3 제출 시 solve


from collections import deque
def bfs(x, idx):
    queue = deque([x])
    stack = [x]
    while queue:
        x = queue.popleft()
        for y in arr[idx:]:
            idx = int(y**(1/2))
            if sum(stack) + y < n and len(stack)<4:
                queue.append(idx)
                stack.append(y)
            elif sum(stack) + y == n:
                return stack + [y]
            
n = int(input())
arr = [i**2 for i in range(int(n**(1/2)), 0, -1)]
result = []
for idx, x in enumerate(arr):
    if x==n: # 더 탐색 안해도 됨
        print(1)
        break

    tmp = bfs(x, idx)
    if tmp:
        result.append(tmp)
else:
    result.sort(key= lambda x:len(x))
    # print(result)
    print(len(result[0]))
# 57% 틀렸습니다

'''
파이썬 특정 값이 되는 숫자 조합 구하는 코드 참고함 https://www.mycompiler.io/view/FQqCmH4Acbf
10:04~24 (20m) 16%쯤 시간초과

from itertools import combinations

def find_combinations():
    for r in range(1, len(lst)+1):
        for combo in combinations(lst, r):
            if sum(combo)==n:
                print(len(combo))
                return

n = int(input())
lst = []
for i in range(int(n**(1/2)), 0, -1):
    lst.append(i**2)

find_combinations()

[게시판]
DP, bfs로 푼 경우 발견
상당한 레벨의 정수론 지식을 가지고 있다면, DP를 안 쓰고 풀 수도 있습니다.

11:25~41, 12:53~1:05, 1:58~08 (38m) 46% 쯤 틀렸습니다
bfs로 구현해봄
기존 bfs 방식 그대로 visited를 쓰면 같은 숫자를 여러번 고려하지 못함

틀린 이유 질문 : https://www.acmicpc.net/board/view/143464
반례 : 27532
[출력] 4
[정답] 3 (26*26 + 66*66 + 150*150) 676+4356+22500
y를 탐색할 떄 함수 input인 x보다 작은 값들을 탐색하도록 수정함
arr 전체를 탐색하게 되면 이전과 중복되는 경우 많음, 그리고 반례를 생각해보면 고려되지 못하는 경우도 생기는 듯
이렇게 했을 때 반례가 정답이 나오긴 하는데, 구성이 좀 다름 10404(102)+10404+6724(82)
57% 틀렸습니다

'''