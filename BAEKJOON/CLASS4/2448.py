# Solved (1h)
triangle = ['  *  ', ' * * ', '*****']
def draw(n):
    if n == 3:
        return triangle
    
    arr = []
    mini = draw(n//2)
    for m in mini:
        arr.append(' '*(n//2) + m + ' '*(n//2))
    for m in mini:
        arr.append(m + ' ' + m)
    return arr
    
N = int(input())
star = draw(N)
for s in star:
    print(''.join(s))
'''
접근 방법 Hint in 질문 게시판
각 좌표 (y, x) 마다 별을 출력하거나 공백을 출력해야 합니다.
현재 단계를 n이라 할 때, f(y, x, n)을 단계 n을 기준으로 좌표 (y, x)에 출력할 문자를 반환하는 함수라고 합시다.
이 f(y, x, n)이 실제로 별 또는 공백 중 하나로 결정되기까지의 과정을 재귀적으로 잘 만들면 됩니다.
1:23~32, 3:08~32 (33m) 규칙을 도저히 못찾겠어서, 조금 더 쉬운 다른 별 찍기 문제 풀어보고자 함

11:28~31 (1h) 2447번과 유사한 방식으로 해결!
'''