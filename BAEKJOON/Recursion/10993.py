# Solved (2h 25m)
def draw(n, x, y):
    if n==1:
        grid[y][x] = '*'
        return

    height = 2**n-1
    width =  4*(2**(n-1))-3
    mid = width//2
    if n%2==1:
        for i in range(width):
            grid[y+height-1][x+i] = '*'
        for i in range(height):
            grid[y + i][x + mid - i] = '*'
            grid[y + i][x + mid + i] = '*'
            
        draw(n-1, x+4*(2**(n-3)), y+(2**(n-1)-1))

    else:
        for i in range(width):
            grid[y][x+i] = '*'
        for i in range(height):
            grid[y + i][x + i] = '*'
            grid[y + i][x + width - 1 - i] = '*'
                
        draw(n-1, x+2**(n-1), y+1)

    

N = int(input())
grid = [[' ' for _ in range(4*(2**(N-1))-3)] for _ in range(2**N-1)]
draw(N, 0, 0)
for c in grid:
    print(''.join(c).rstrip())

'''
식 구하기, grid index 지정 부분에서 시간 많이 소요됨

if i <= mid:
    grid[y+height-1-i][x+i] = '*'
elif mid+1 < i < width+1:
    grid[y-height+i][x+i-1] = '*'

> 높이 따라가면서 좌우 대각선 별채우기 부분 index 고려 너무 복잡해서 아래와 같이 단순화    

for i in range(height):
    grid[y + i][x + mid - i] = '*'
    grid[y + i][x + mid + i] = '*'
'''