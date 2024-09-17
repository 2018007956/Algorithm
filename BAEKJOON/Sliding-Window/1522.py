# Solved (30m)
arr = input()

a_cnt = arr.count('a')
min_b_cnt = 500
for i in range(len(arr)):
    cur = arr[i:i+a_cnt]
    b_cnt = cur.count('b')
    if i > len(arr)-a_cnt:
        b_cnt += arr[:a_cnt-len(cur)].count('b')
    min_b_cnt = min(min_b_cnt, b_cnt)

print(min_b_cnt)