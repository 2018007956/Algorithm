# Solved (15m)
def dfs(depth, equ):
    if depth==N:
        if eval(equ.replace(' ',''))==0:
            result.append(equ)
        return

    cur = str(depth+1)
    dfs(depth+1, equ+'+'+cur)
    dfs(depth+1, equ+'-'+cur)
    dfs(depth+1, equ+' '+cur)


t = int(input())
for _ in range(t):
    N = int(input())
    result = []
    dfs(1, '1')
    for equation in sorted(result):
        print(equation)
    print()

'''
문자열 수식 계산하는 함수 : eval
'''