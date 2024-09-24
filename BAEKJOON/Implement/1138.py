# 풀이 공부
# Sol 1
N = int(input())
arr = list(map(int, input().split()))

result = [0] * N
for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == arr[i] and result[j]==0:
            result[j] = i + 1
            break
        elif result[j] == 0:
            cnt += 1

print(*result)

# Sol 2
result = []
for i in range(N, 0, -1):
    result.insert(arr[i-1], i)

print(*result)
'''
3:33~04 (30m) 풀이 참고
    큰 사람이 왼쪽에 몇 명이 있어야 하는지 주어진 값을 보고 그만큼의 빈자리를 비워 둔 후에 값 채우기

~15 (11m) 틀렸습니다
    그 자리에 배치할 수 있는 조건이 "비어 있음"이 아니라 "앞에 있는 사람 수를 만족하는 자리"여야 함
'''