#20173

n = input()
P = list(map(int, input().split()))

r1 = [0 for x in range(n+1)]
for i in P:
    for j in P:
        if i-j>=2:
            r1[i]+=1
        else:
            r1[j]+=1

# Calculate D

'''
문제 이해도 잘 안됨
다른 풀이 보고 공부해보기

'''