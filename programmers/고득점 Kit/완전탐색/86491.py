# Solved (5m)
def solution(sizes):
    wallet_x, wallet_y = 0, 0 # x: 가로, y: 세로
    for x, y in sizes:
        if x >= y: 
            wallet_x = max(wallet_x, x)
            wallet_y = max(wallet_y, y)
        else:
            wallet_x = max(wallet_x, y)
            wallet_y = max(wallet_y, x)
    return wallet_x * wallet_y



# 다른 사람 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col


solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
# sum(sizes, []) : 2차원 배열을 1차원으로 만들기