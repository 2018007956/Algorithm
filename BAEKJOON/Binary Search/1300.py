# 풀이 공부
N = int(input())
k = int(input())

start, end = 0, k
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N)

    if temp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
'''
* 각 행별로 x보다 작거나 같은 수의 개수는 x를 행으로 나눈 몫이다
    위를 생각해 낼 수 있다면, 각 행별로 돌아가며 x보다 작거나 같은 수들의 개수를 세면서 이분 탐색 수행
    k번째 숫자가 무엇인지를 알 수 있음 
'''