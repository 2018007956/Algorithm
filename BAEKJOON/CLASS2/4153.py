while True:
    num = list(map(int, input().split()))
    if num == [0,0,0]:
        break
    num.sort()
    print('right' if num[0]**2 + num[1]**2 == num[2]**2 else 'wrong')