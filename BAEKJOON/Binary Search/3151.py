# 풀이 공부
import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0
for start in range(N):
    mid, end = start+1, N-1
    while mid < end:
        cur = arr[start] + arr[mid] + arr[end]
        if cur == 0:
            if arr[mid] == arr[end]:
                cnt += end - mid
            else:
                idx = bisect.bisect_left(arr, arr[end])
                cnt += end - idx + 1
            mid += 1

        elif cur < 0:
            mid += 1
        else:
            end -= 1

print(cnt)

'''
2:07~32 (25m) 2% 틀렸습니다
반례
8
-10 5 5 5 5 5 5 5
[정답] 21
[출력] 6

6
-8 3 3 5 5 5
[정답] 6
[출력] 2

3:50~4:27 풀이 공부, python 4%? 시간초과 pypy Solved
    bisect를 이용해서 중복되는 수의 개수를 한 번에 더해준다
    Ref) https://velog.io/@030831/%EB%B0%B1%EC%A4%80-3151-%ED%95%A9%EC%9D%B4-0-Python
'''