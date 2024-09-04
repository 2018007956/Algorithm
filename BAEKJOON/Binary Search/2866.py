# Solved (40m)
import sys
input = sys.stdin.readline
R, C = map(int, input().split())
table = [input() for _ in range(R)]

res = 0
start, end = 0, R-1
while start <= end:
    mid = (start + end) // 2
    
    tmp = set()
    rotate = list(zip(*table[mid:]))
    for i in range(C):
        tmp.add(''.join(rotate[i]))

    if len(tmp) >= C:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
'''
7:00~11, 20~31 (22m) 3% 시간 초과
    풀이 참고 -> 전체를 확인 후 길이 비교를 하는게 아니라, 같은게 들어오면 바로 종료하도록 구현
    
37~50 (13m) 4%? 시간 초과
    s = ''.join(list(zip(*table[mid:]))[i]) 이 코드를 아래와 같이 수정
    for j in range(mid, R):
        s += str(table[j][i])

    //// list(zip(*table[mid:])) 이걸 한번만 수행하도록 수정 
        => 위 코듲보다 시간 더 단축됨
        => 중복되면 바로 종료되도록 구현하지 않아도 Solved

~55 Solved
**반복문 밖에서 정의해도 되는데, 안에 정의하여 불필요한 동작을 반복수행하고 있진 않은지 항상 확인 필요**
'''