# 2024-04-23
def count_diff(arr):
    # 1: 왼쪽 위가 W인 경우
    ans = ['WBWBWBWB', 'BWBWBWBW']
    cnt_w = 0
    k=0
    for i in range(8):
        for j in range(8):
            if arr[i][j]!=ans[k][j]:
                cnt_w += 1
        k+=1
        k%=2

    # 2: 왼쪽 위가 B인 경우
    cnt_b = 0
    k=1
    for i in range(8):
        for j in range(8):
            if arr[i][j]!=ans[k][j]:
                cnt_b += 1
        k+=1
        k%=2
    return min(cnt_w, cnt_b)

# Input
N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(input())

# Bruth force
result = []
for i in range(N-7):
    for j in range(M-7):
        result.append(count_diff([row[j:j+8] for row in board[i:i+8]]))
print(min(result))

'''
5:10~6:00 (50m) 생각한대로 다 구현했는데 Index Error 뜨는 상황
4:42~11:02 (20m)
    문제 : 2차원 배열 slicing이 제대로 안됨
    해결 : board[i:i+8][j:j+8] -> [row[j:j+8] for row in board[i:i+8]]

작년에 풀어서 틀렸던 아래 코드도 같은 문제였음. 해당 부분 수정하니 성공
'''

# 2023-01-06
N, M = map(int, input().split())

def start_(i, s):
    cnt = []
    if i%2 == 0:
        case = str(s*M)[:M]
    else:
        case = str(s[::-1]*M)[:M]

    for j in range(M):
        if lst[j] != case[j]:
            cnt.append(1)
        else:
            cnt.append(0)
    return cnt

start_w = []
start_b = []
for i in range(N):
    lst = input()
    # 왼쪽 위가 W인 경우
    start_w.append(start_(i, 'WB'))
    # 왼쪽 위가 B인 경우
    start_b.append(start_(i, 'BW'))
    
# 8X8
result = []
for i in range(N-8+1):
    for j in range(M-8+1): 
        w = sum(sum([row[j:j+8] for row in start_w[i:i+8]], []))
        b = sum(sum([row[j:j+8] for row in start_b[i:i+8]], []))
        result.append(min(w,b))
print(min(result)) 

'''
sum([[1,2],[3,4]]) 로 하면 start의 값이 디폴드로 0이기 때문에, 
TypeError: unsupported operand type(s) for +: 'int' and 'list' 에러 발생
(sum 함수가 첫 번째 인자로 0을 사용하고, 두번째 인자부터 주어진 반복 가능한 컬렉션의 각 요소들을 0에 더함)

sum([[1,2],[3,4]], []) 의 형태로 사용해야 [] + [1,2] + [3,4]로 해석되어 
[1,2,3,4]라는 1차원 리스트를 구할 수 있다
'''