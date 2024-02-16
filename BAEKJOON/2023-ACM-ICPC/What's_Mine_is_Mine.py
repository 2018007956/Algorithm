#17979

m, n = map(int, input().split())

price = []
for i in range(m):
    price.append(input())

type = [0 for x in range(m)]
for i in range(n):
    s,e,t = map(int, input().split())
    mineral_amount = e-s
    earn = mineral_amount * t 
    
    if type[t-1]:
        type[t-1] = max(type[t-1],earn)
    

print(type)
print(sum(type))