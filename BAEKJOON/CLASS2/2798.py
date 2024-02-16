from itertools import combinations
N, M = map(int, input().split())
lst = list(map(int, input().split()))

biggest_sum = 0
for cards in combinations(lst, 3):
    temp_sum = sum(cards)
    if biggest_sum < temp_sum <= M:
        biggest_sum = temp_sum
print(biggest_sum)

'''
런타임에러원인
1. 배열 인덱스 범위를 벗어났을 경우
2. 0으로 나눌 때
3. 사용하는 라이브러리에서 예외를 발생시켰을 때
4. 재귀 호출이 너무 길어질 때

if i<=0 and i>m: 에 안걸려서 diff.index[-9999]가 들어가버림
전부 M보다 커서 양수만 있는 경우가 있을 수 있음
-> if m != -9999: 일떄 출력 -> 틀림

filter나 리스트를 새로 생성해버리면 original index가 안들어감

c = list(combinations(lst, 3))
sum_c = list(map(sum, c))

diff = list(map(lambda x:x-M, sum_c))
# 음수 중 가장 큰 수
m = -9999
for i in diff:
    if i<=0 and i>m:
        m = i

if m != -9999:
    print(sum_c[diff.index(m)])

내 코드에선 왜 틀린지 모르겠음
다른 사람 코드보니까
sum을 하면서 바로 비교해서 biggest 값 출력
굳이 리스트 중에 큰 수 찾아서 index로 다시 찾고 출력하는게 아니라
이렇게 하는게 훨씬 효율적
'''