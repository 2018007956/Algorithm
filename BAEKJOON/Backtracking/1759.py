# Solved (30m) w/ Search
L, C = map(int, input().split())
arr = input().split()
arr.sort()
result = []

def dfs(idx):
    if len(result)==L:
        vowel, consonant = 0, 0
        for x in result:
            if x in ['a', 'e', 'i', 'o', 'u']:
                vowel += 1
            else:
                consonant += 1
        
        if vowel >= 1 and consonant >=2:
            print(''.join(result))

    for i in range(idx, C):
        result.append(arr[i])
        dfs(i+1)
        result.pop()
    
dfs(0)

'''
# Solved (13m) - 조합 풀이
from itertools import combinations
L, C = map(int, input().split())
arr = input().split()
arr.sort()
for x in sorted(combinations(arr, L)):
    vowel = 0 #모음    
    consonant = 0 # 자음
    for i in x:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            vowel += 1
        else:
            consonant += 1
    
    if vowel >= 1 and consonant >=2:
        print(''.join(x))
'''