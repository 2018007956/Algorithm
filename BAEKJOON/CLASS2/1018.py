N, M = map(int, input().split())

def start_(i, s):
    cnt = []
    if i==0 or i%2 == 0: # 홀수번째 row
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
print(len(start_w), len(start_w[0]))
result = []
for i in range(N-8+1): # 0~2
    for j in range(M-8+1): # 0~16
        w = sum(sum(start_w[i:i+8][j:j+8], []))
        b = sum(sum(start_b[i:i+8][j:j+8], []))
        result.append(min(w,b))
        print('i,j:',i,j,i+8, j+8)
        print('len:',len(start_w[i:i+8][j:j+8]))
        print(start_w[i:i+8][j:j+8])
print(min(result)) 

'''
sum([[1,2],[3,4]]) 로 하면 start의 값이 디폴드로 0이기 때문에, 
TypeError: unsupported operand type(s) for +: 'int' and 'list' 에러 발생
sum([[1,2],[3,4]], []) 의 형태로 사용해야 [] + [1,2] + [3,4]로 해석되어 
1차원 리스트를 구할 수 있다
'''