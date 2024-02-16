N = int(input())
cnt = 0
six_n = 0
while True:
    if "666" in str(cnt):
        six_n += 1
    if six_n == N:
        print(cnt)
        break
    cnt +=1