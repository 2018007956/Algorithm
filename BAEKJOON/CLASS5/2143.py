# 풀이 공부
import bisect

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_cumulate = []
B_cumulate = []

for i in range(n):  #O(A*(A-1)/2) = O(N^2)
    s = A[i]
    A_cumulate.append(s)
    for j in range(i+1,n):
        s += A[j]
        A_cumulate.append(s)

for i in range(m):  #O(B*(B-1)/2)  = O(M^2)
    s = B[i]
    B_cumulate.append(s)
    for j in range(i+1,m):
        s += B[j]
        B_cumulate.append(s)
        
A_cumulate.sort()
B_cumulate.sort()

ans = 0
for x in A_cumulate:
    l = bisect.bisect_left(B_cumulate, T-x)
    r = bisect.bisect_right(B_cumulate, T-x)
    ans += r-l
print(ans)
'''
10:30~11:06 (36m) 풀이 감을 못잡음

4:36~5:08 (32m) 풀이 공부 (참고: https://imksh.com/78)
내가 상상치도 못한 풀이다 충격
    1. 각 위치별로 누적합을 구해서 배열 생성
    2. 같은 수는 개수만큼 카운트 되므로 -> 정렬해서 그 개수만큼 ans에 더해줌
'''