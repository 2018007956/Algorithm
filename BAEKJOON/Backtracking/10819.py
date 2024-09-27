# Solved (13m) w/ Search
# Sol 1) 라이브러리 사용
from itertools import permutations
N = int(input())
A = list(map(int, input().split()))

result = 0
for arr in permutations(A):
    cal = 0
    for j in range(1, N):
        cal += abs(arr[j-1]-arr[j])
    
    result = max(result, cal)

print(result)

# Sol 2) permutations을 백트래킹으로 직접 구현
def permutations(new_arr):
    global result
    if len(new_arr) == N:
        cal = 0
        for j in range(1, N):
            cal += abs(new_arr[j-1]-new_arr[j])
        result = max(result, cal)
        return

    for i in range(len(A)):
        if not visited[i]:
            visited[i] = True
            permutations(new_arr + [A[i]])
            visited[i] = False

N = int(input())
A = list(map(int, input().split()))

visited = [False] * N
result = 0
permutations([])
print(result)