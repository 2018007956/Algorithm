# Solved (50m) w/ Search
N = int(input())
arr = list(map(int, input().split()))

cnt = 0
end = 0
cur = set()
for start in range(N):
    while end <= N-1 and arr[end] not in cur:
        cur.add(arr[end])
        end += 1
    cnt += (end-start)
    cur.remove(arr[start])

print(cnt)
'''
10:41~11 (30m) 시간 초과
    list indexing 대신 cur = [] 사용
    while 루프 내에서 set()을 계속 생성하는 부분 비효율적
    수정 전 코드
    if len(set(cur))==len(cur):
        cnt += 1
    수정 후 코드 : **end를 증가하는 조건문에 해당 숫자가 있는지 확인**
    while arr[end] not in cur
    cnt += (end-start)

    in 연산은 list에 할 땐 O(N)인데, set에 할 땐 O(1)
    arr -> set으로 수정

    **end를 for문 안에서 end = start로 정의하지 않고, 밖에서 end=0으로 정의하면 
    같은 수가 등장하지 않는 연속한 수를 찾는 탐색과정을 여러번 수행하지 않을 수 있음**

~31 (20m) Solved
'''