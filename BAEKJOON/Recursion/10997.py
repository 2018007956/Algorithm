# Solved (29m)
N = int(input())
grid = [[' ' for _ in range(4*N-3)] for _ in range(4*N-1)]
def draw(n, x, y):
    if n == 1:
        grid[y][x] = '*'
        return

    width = 4*n-3
    height = width+2
    # 바깥 가로
    for i in range(width):
        grid[y][x+i] = '*'
        grid[y+height-1][x+i] = '*'
    # 바깥 왼쪽 세로
    for i in range(height):
        grid[y+i][x] = '*'
    # 바깥 오른쪽 세로
    for i in range(height-2):
        grid[y+2+i][x+width-1] = '*'
    # 안쪽 가로
    for i in range(width-2):
        grid[y+2][x+2+i] = '*'
    # 안쪽 세로
    for i in range(height-4):
        grid[y+2+i][x+2] = '*'

    draw(n-1, x+2, y+2)


draw(N, 0, 0)

for c in grid:
    print(''.join(c).rstrip())