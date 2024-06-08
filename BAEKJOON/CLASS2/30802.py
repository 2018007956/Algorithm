# Solved (13m)
import math
N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
print(sum([math.ceil(x/T) for x in size]))
print(sum(size)//P, sum(size)%P)