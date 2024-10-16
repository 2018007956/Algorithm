# Solved (30m) w/ Search
def is_good(x):
    for k in range(1, len(x)//2+1):
        if x[-k:] == x[-2*k:-k]:
            return False
    return True

def dfs(depth, x):
    if depth==N:
        print(x)
        exit()
    
    for num in range(1, 4):
        if is_good(x+str(num)):
            dfs(depth+1, x+str(num))


N = int(input())
dfs(0, '')
'''
if x=='' or (x and x[-1] != str(num)) and (len(x)>=3 and x[-3:-1] != x[-1]+str(num)) and (len(x)>=5 and x[-5:-2] != x[-2:]+str(num)):
초음엔 조건문을 위와 같이 생각함
1,2,3으로만 이루어져서 길이 6까지 체크하면되겠다 생각했는데, 더 긴 길이도 가능
=> 마지막 k 길이의 부분 수열이 그 전부분 수열과 같은지를 체크하는 것으로 수정

12:16~43 (27m) 시간초과
    1, 2, 3 순서대로 탐색하기 때문에, 종료 조건을 만족하면 바로 exit

~46 (3m) Solved
'''