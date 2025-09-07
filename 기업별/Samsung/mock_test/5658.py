T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    s = input()

    length = n // 4
    nums = set()
    for i in range(length):
        for a in range(0, len(s), length):
            nums.add(s[a:a+length])
        s = s[-1] + s[:-1]
    
    nums = sorted([int(x, 16) for x in nums], reverse=True)
    print(f'#{t} {nums[k - 1]}')