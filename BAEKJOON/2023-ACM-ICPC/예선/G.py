import sys
input = sys.stdin.readline

n,k = map(int, input().split())
dict = {0.0:"0 1"}

for i in range(1,n):
    for j in range(i,n+1):
        # if i/j not in dict.keys():
        if j%i==0 and i!=1:
            continue 
        dict[i/j]=f'{i} {j}'

dict = sorted(dict.items())

#print(dict)
#print(dict[k-1][1])
print(dict)
a = int(dict[k-1][1][0])
b = int(dict[k-1][1][-1])
print(a,b)