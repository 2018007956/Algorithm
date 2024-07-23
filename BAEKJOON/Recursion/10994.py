# Solved (52m) w/ Search
N = int(input())
grid = [[' ' for _ in range(4*(N-1)+1)] for _ in range(4*(N-1)+1)]
def draw(n, x, y):
    if n == 1:
        grid[y][x] = '*'
        return
    
    length = 4*(n-1)+1
    for i in range(length):
        grid[y][x+i] = '*'
        grid[y+i][x] = '*'
        grid[y+length-1][x+i] = '*'
        grid[y+i][x+length-1] = '*'

    draw(n-1, x+2, y+2)

# Fill the grid
draw(N, 0, 0)

for c in grid:
    print(''.join(c))

'''
3:35~17 (42m) 갈피를 못잡아서 풀이 참고
~27 (10m) Solved
'''