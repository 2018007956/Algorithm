# Not solved
def Z(n, r, c):
    if n == 0:
        return 0
    cnt = 2 * (r%2) + (c%2)
    return 4 * Z(n-1, r//2, c//2) + cnt

N, r, c = map(int, input().split())
print(Z(N, r, c))

'''
9:6~37 (30m) 도저히 감도 안잡혀서 풀이 공부
Ref) https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-1074-Z
표의 규칙 찾기!
Ref2) https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-1074-Z
사분면 나눠서 count
'''