# Solved (29m)
N = int(input())
grid = [[' ' for _ in range(4*N-3)] for _ in range(2*N-1)]
for i in range(N):
    # head, tail
    grid[0][i] = '*'    # 1
    grid[-1][i] = '*'   # 2
    grid[0][3*N-3+i] = '*'  # 3
    grid[-1][3*N-3+i] = '*' # 4

    # left and right body
    grid[i][i] = '*'    # 5
    grid[2*N-2-i][i] = '*' # 6
    grid[i][4*N-4-i] = '*' # 7
    grid[-1-i][4*N-4-i] = '*'   # 8

    # center
    grid[i][i+N-1] = '*'    
    grid[2*N-2-i][i+N-1] = '*' 
    grid[i][4*N-4-i-(N-1)] = '*' 
    grid[-1-i][4*N-4-i-(N-1)] = '*' 


for c in grid:
    print(''.join(c).rstrip())

'''
출력 형식 오류가 떠서 왜 그런지 봤더니 (질문게시판 참고)
각 줄의 마지막 별 뒤에 불필요한 공백이 출력되는 것이 문제였다.
모든 줄이 동일한 수의 문자를 출력하는 것이 아니라 마지막으로 나타나는 별까지만 출력하고 바로 다음 줄로 넘어가야 함
예제 출력 드래그 해보기
-> rstrip() 사용

다른 풀이: grid 초기화 시킬 필요 없이 for문 돌면서 규칙에 맞게 바로 출력
'''