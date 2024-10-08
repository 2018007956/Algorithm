# 풀이 공부
def dfs(depth, cur_num):
    global min_val, max_val
    if depth==k+1:
        min_val = min(min_val, int(cur_num))
        max_val = max(max_val, int(cur_num))
        return
    
    for i in range(10):
        if not visited[i]:
            if depth == 0 or (giho[depth-1]=='>' and cur_num[-1] > str(i)) or (giho[depth-1]=='<' and cur_num[-1] < str(i)):
                visited[i] = True
                dfs(depth+1, cur_num + str(i))
                visited[i] = False
                

k = int(input())
giho = input().split()

visited = [False] * 10
min_val = 10**(k+1)
max_val = 0

dfs(0, "")

print(str(max_val).zfill(k+1))
print(str(min_val).zfill(k+1))