# Solved (9m)
N, K = map(int, input().split())
arr = list(map(int, input().split()))

part_sum = sum(arr[:K])
max_val = part_sum
for i in range(K, N):
    part_sum += arr[i] - arr[i-K]
    max_val = max(max_val, part_sum)
print(max_val)