# Solved (18m)
import sys
input = sys.stdin.readline
nA, nB = map(int, input().split())
A, B = {}, {}
for n in map(int, input().split()):
    A[n] = 1
for n in map(int, input().split()):
    B[n] = 1

# 리스트로 풀면 시간초과가 나지만 해쉬로 풀면 문제를 해결할 수 있다.
C = []
for a in A:
    if a not in B:
        C += [a]

print(len(C))
print(*sorted(C))

# Sol2) set
nA, nB = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A-B))
print(*sorted(A-B))


'''
# 어차피 A의 모든 원소 다 탐색해야 하는데 이분 탐색 왜 씀? A 원소를 하나씩 돌면서 B에 존재하는지 빠르게 탐색
그치만 더 편한 방식으로 구현해봄
리스트 not in 사용 코드의 시간복잡도 : 500,000 * 500,000 = 250000000000 시간 초과 예상
hash map으로 다시 구현
'''
