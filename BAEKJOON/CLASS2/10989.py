import sys
N = int(input())

arr = [0] * 10001
for i in range(N):
    arr[int(sys.stdin.readline())] += 1

# # arr.sort() # -> 메모리 초과
for i in range(1, 10001):
    if arr[i] != 0:
        for cnt in range(arr[i]):  # 개수만큼 출력
            print(i)