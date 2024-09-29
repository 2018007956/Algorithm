# Solved (13m)
N = int(input())
result = 0
for i in range(1, len(str(N))):
    result += 9*10**(i-1)*i
result += (N - 10**(len(str(N))-1) +1) * len(str(N))
print(result)