# Solved (30m) w/ Search
N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

max_val = -1e9
min_val = 1e9

def dfs(i, val):
    global add, sub, mul, div, max_val, min_val
    if i==N:
        max_val = max(max_val, val)
        min_val = min(min_val, val)    
    
    if add > 0:
        add -= 1
        dfs(i+1, val+arr[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i+1, val-arr[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i+1, val*arr[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i+1, int(val/arr[i]))
        div += 1


dfs(1, arr[0])

print(int(max_val))
print(int(min_val))