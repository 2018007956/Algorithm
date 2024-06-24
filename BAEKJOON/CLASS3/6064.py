# 풀이 공부
T = int(input())
for _ in range(T):
    M,N,x,y = map(int, input().split())

    year = x
    while year<=M*N:
        if (year-x) % M == 0 and (year-y) % N == 0:
            print(year)
            break
        year += M
    else:
        print(-1)

'''
종료 조건을 어떻게 줘야할까?
while year <= M*N 라고하면 최대 시간복잡도가 1600000000=1.6*10^9
PyPy3 으로 제출해봤는데 3% 시간초과 (27m)

14~32 (18m) 풀이 공부
    종료 조건은 잘 세워줬는데, year-x가 M의 배수라는 성질을 못 발견했다
'''