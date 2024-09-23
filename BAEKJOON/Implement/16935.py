# Solved (46m)
import sys
input = sys.stdin.readline
def flip_upside_down(A):
    return A[::-1]

def flip_left_right(A):
    return [a[::-1] for a in A]

def rotated_right_90(A):
    return list(map(list, zip(*A[::-1])))

def rotated_left_90(A):
    return [a[::-1] for a in list(map(list, zip(*A[::-1])))[::-1]]

def rotated_right_quater(A):
    N = len(A)
    M = len(A[0])
    # 왼쪽 상단 저장
    tmp = [a[:M//2] for a in A[:N//2]]
    # 왼쪽 하단을 왼쪽 상단으로 복사
    for i in range(N//2, N):
        for j in range(M//2):
            A[i-N//2][j] = A[i][j]
    # 오른쪽 하단을 왼쪽 하단으로 복사
    for i in range(N//2, N):
        for j in range(M//2, M):
            A[i][j-M//2] = A[i][j]
    # 오른쪽 상단을 오른쪽 하단으로 복사
    for i in range(N//2):
        for j in range(M//2, M):
            A[i+N//2][j] = A[i][j]
    # 왼쪽 상단(tmp)을 오른쪽 상단으로 복사
    for i in range(N//2):
        for j in range(M//2):
            A[i][j+M//2] = tmp[i][j]
    return A

def roated_left_quater(A):
    N = len(A)
    M = len(A[0])
    # 왼쪽 상단 저장
    tmp = [a[:M//2] for a in A[:N//2]]
    # 오른쪽 상단을 왼쪽 상단으로 복사
    for i in range(N//2):
        for j in range(M//2, M):
            A[i][j-M//2] = A[i][j]
    # 오른쪽 하단을 오른쪽 상단으로 복사
    for i in range(N//2, N):
        for j in range(M//2, M):
            A[i-N//2][j] = A[i][j]
    # 왼쪽 하단을 오른쪽 하단으로 복사
    for i in range(N//2, N):
        for j in range(M//2):
            A[i][j+M//2] = A[i][j]
    # 왼쪽 상단(tmp)을 왼쪽 하단으로 복사
    for i in range(N//2):
        for j in range(M//2):
            A[i+N//2][j] = tmp[i][j]
    return A


N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
num = list(map(int, input().split())) 

for x in num:
    if x==1:
        A = flip_upside_down(A)
    elif x==2:
        A = flip_left_right(A)
    elif x==3:
        A = rotated_right_90(A)
    elif x==4:
        A = rotated_left_90(A)
    elif x==5:
        A = rotated_right_quater(A)
    elif x==6:
        A = roated_left_quater(A)

for line in A:
    print(*line)

'''
9:03~43 (40%) 8%쯤 런타임에러 (IndexError)
    rotate_90 해서 가로 세로 길이가 달라졌는데, 인덱스 접근하는 연산을 하는 경우 고려
    => rotate_quater에서 N, M 재지정

~49 (6m) Solved
'''