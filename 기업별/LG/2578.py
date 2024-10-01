# Solved (31m)
from itertools import chain

def bingo_check(called):
    bingo = 0
    # 행 체크
    for y in range(5):
        if all(called[y]):
            bingo += 1
    # 열 체크
    for x in range(5):
        if all([row[x] for row in called]):
            bingo += 1
    # 대각선 체크
    if all([called[y][x] for y, x in zip(range(5), range(5))]):
        bingo += 1
    if all([called[y][4-x] for y, x in zip(range(5), range(5))]):
        bingo += 1

    return bingo


board = [list(map(int, input().split())) for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]

def solution():
    board_flat = list(chain.from_iterable(board))
    called = [[False] * 5 for _ in range(5)]
    for i, row in enumerate(arr):
        for j, num in enumerate(row):
            idx = board_flat.index(num)
            called[idx//5][idx%5] = True
            if bingo_check(called)>=3:
                print(5*i + j+1)
                return

solution()

'''
10:00~28 (28m) 20% 틀렸습니다
    한번에 투빙고가 추가되는 경우가 있을 것. bingo_check 조건을 ==3이 아니라 >=3로 수정

~31 (3m) Solved
'''