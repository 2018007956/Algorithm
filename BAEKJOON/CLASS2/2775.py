T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    f0 = [i for i in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            f0[j] += f0[j-1]    
    print(f0[-1])


'''
f0 = [1,2,3,4,...]
f1 = [1,3,6,10,...]
f2 = [1,4,10,20,...]
'''