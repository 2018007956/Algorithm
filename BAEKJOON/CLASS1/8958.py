N = int(input())
for i in range(N):
    str_OX = input()
    cnt = 0
    result = 0
    for j in str_OX:
        if j == 'O':
            cnt += 1
        else:
            cnt = 0
        result += cnt
    print(result)