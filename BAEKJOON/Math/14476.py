# 풀이 공부
import math
N = int(input())
arr = list(map(int, input().split()))

prefix = [0] * (N+1)
suffix = [0] * (N+1)

prefix[0] = arr[0]
for i in range(1, N):
    prefix[i] = math.gcd(prefix[i-1], arr[i])

suffix[N-1] = arr[N-1]
for i in range(N-2, -1, -1):
    suffix[i] = math.gcd(suffix[i+1], arr[i])

result_gcd = []
for i in range(N):
    res = math.gcd(prefix[i-1], suffix[i+1])
    if arr[i] % res !=0:
        result_gcd.append((res, arr[i]))

result_gcd.sort(reverse=True)
print(' '.join(map(str, result_gcd[0])) if result_gcd else -1)