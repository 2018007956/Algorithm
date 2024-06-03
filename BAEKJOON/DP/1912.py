# Solved (18m)
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
for i in range(1,n):
    dp.append(max(arr[i], dp[i-1]+arr[i]))
print(max(dp))

'''
6:31~41, 9:31~49 (28m) 2% 메모리초과

메모리 초과를 어떻게 개선해야 할까..
result 배열 대신 변수 선언
11:08~14 (6m) 2% 시간초과

코드 에러 수정 : cumulate에 0 넣고 시작, 마지막에 arr 따로 고려해주는 부분 제거
11:20~34 (14m) 2% 시간초과

11:54~ 05, 8:44~53 (20m)
100000! = 매우 큰 숫자이기 때문에 아래와 같은 이중 포문을 사용하면 안됨

n = int(input())
arr = list(map(int, input().split()))
cumulate = [0] # 0 넣어줘야 누적합(j-i)에 대해서 젤 첫번째 수가 i일 때가 고려됨, 하나 선택되는 경우를 따로 안고려해줘도 됨
for x in arr:
    cumulate.append(cumulate[-1]+x)

result = -1e8
tmp = []
for idx, i in enumerate(cumulate):
    for j in cumulate[idx+1:]:
        if j-i>result:
            result = j-i
print(result)

지금 이렇게 푼 건 브루트 포스고, dp를 쓸 수 있도록 반복되는 구조가 있는지 생각해보자.
(정답 코드 확인) https://data-marketing-bk.tistory.com/entry/%EB%B0%B1%EC%A4%80-1912%EB%B2%88-%EC%97%B0%EC%86%8D%ED%95%A9%ED%8C%8C%EC%9D%B4%EC%8D%AC
    arr을 탐색하면서 기존의 값과 직전 원소와의 합의 값을 비교하면서 업데이트 해주면서 탐색
    즉, 이전까지의 모든 숫자의 합 중 최대값을 그때그때 기록하는 방법 

다음에 다시 도전 -> Solved in 18m
'''