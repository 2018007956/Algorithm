# import bisect

# T = int(input())
# n = int(input())
# A = list(map(int, input().split()))
# m = int(input())
# B = list(map(int, input().split()))

# A_cumulate = []
# B_cumulate = []

# for i in range(n):  #O(A*(A-1)/2) = O(N^2)
#     for j in range(i+1,n+1):
#         A_cumulate.append(sum(A[i:j]))

# for i in range(m):  #O(B*(B-1)/2)  = O(M^2)
#     for j in range(i+1,m+1):
#         B_cumulate.append(sum(B[i:j]))

# A_cumulate.sort()
# B_cumulate.sort()

# ans = 0
# for x in A_cumulate:
#     l = bisect.bisect_left(B_cumulate, T-x)
#     r = bisect.bisect_right(B_cumulate, T-x)
#     ans += r-l
# print(ans)

## 또 다른 풀이
# 배열 A의 모든 부 배열의 합을 탐색하며 그 합의 값을 Key로 하고, 그 개수를 값으로하는 딕셔너리(여기선 Counter로 사용)를 c로 만듭니다. 
# 배열 B의 모든 부 배열의 합을 탐색하며, T에서 B의 부 배열합을 뺀 값이 c에 존재하면 그 값을 result에 더해나갑니다. 
from collections import Counter
 
T = int(input()) # 부 배열의 합으로 만족되야 하는 값
n = int(input()) # 배열 A의 원소 개수
A = list(map(int,input().split())) # 배열 A
m = int(input()) # 배열 B의 원소 개수
B = list(map(int,input().split())) # 배열 B
 
result = 0 # 출력할 값 0으로 초기화
c = Counter() # 카운터 c 정의
 
for i in range(n):
    for j in range(i+1,n+1):
        c[sum(A[i:j])] += 1 # 배열 A의 모든 부배열의 합을 카운터에 개수로 센다
print(c)

for i in range(m):
    for j in range(i+1,m+1):
        t = T - sum(B[i:j]) # 타겟 값 T에서 B의 부배열합을 뺀 값이
        result += c[t] # A의 부배열에 존재하면 result에 더해준다. 없으면 저절로 0이 나온다.
print(result)

'''
Counter : 데이터의 개수를 셀 때 유용한 클래스

함수
.most_common() : 데이터 개수가 많은 순으로 정렬된 배열 리턴
.most_common(k) : 가장 개수가 많은 k개의 데이터 리턴
'''