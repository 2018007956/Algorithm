N = int(input())

cnt = 1
tmp = 1
while True:
    if N <= tmp:
        print(cnt)
        break
    tmp = tmp + 6*cnt
    cnt += 1