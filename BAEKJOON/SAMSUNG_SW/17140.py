# Solved (1h 40m) w/ Search
from collections import Counter
from itertools import chain

def sorting(A):
    max_length = 0
    for idx, row in enumerate(A):
        data = Counter(row)
        del data[0]
        data = sorted(data.items(), key=lambda x: (x[1], x[0]))
        A[idx] = list(chain.from_iterable(data))[:100]
        max_length = max(max_length, len(A[idx]))
        
    # 각 행을 가장 긴 길이에 맞추고 빈 공간은 0으로 채우기
    return [row + [0] * (max_length - len(row)) for row in A]

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
r, c = r-1, c-1
time = 0
while time <=100:
    if r<len(A) and c<len(A[0]) and A[r][c]==k:
        print(time)
        break
    
    if len(A) >= len(A[0]):
        A =sorting(A)        
    else:
        A = list(map(list, zip(*A)))
        A = sorting(A)
        A = list(map(list, zip(*A)))

    time += 1
else:
    print(-1)
'''
[알게된 점]
2차원 flatten 
    방법1) itertools의 chain 함수 사용
        여러 iterable을 하나로 연결해주는 기능
        사용법 : list(chain.from_iterable(array))
    방법2) functools의 reduce 함수 사용
        iterable 내 각 요소를 연산한 뒤 이전 연산 결과들과 누적해서 반환해주는 함수
        사용법 : reduce(lambda x, y : list(x) + list(y), array)
        
2차원 리스트의 column 추출 : zip(*array)
    zip 함수는 여러 iterable을 병렬로 묶어주는 기능
'''