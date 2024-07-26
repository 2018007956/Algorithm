# Solved (28m) w/ Search
N = int(input())
square = ['***', '* *', '***']
def draw(n):
    if n == 3:
        return square
    
    ans = []
    mini = draw(n//3)
    for m in mini:
        ans.append(m*3)
    for m in mini:
        ans.append(m + ' '*(n//3) + m)
    for m in mini:
        ans.append(m*3)
    return ans

star = draw(N)
for s in star:
    print(''.join(s))