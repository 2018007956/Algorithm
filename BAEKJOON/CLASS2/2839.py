def bongji(x):
    rn = N - (x*5)
    if x == -1:
        return -1
    elif rn%3 == 0:
        return x + rn//3
    else:
        return bongji(x-1)

N = int(input())
if N%5==0:
    print(N//5)
else:
    print(bongji(N//5))


'''
18//5=3...3
3=18-3*5
'''