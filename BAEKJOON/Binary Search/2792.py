# Solved (53m) w/ Search
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
bosuk = [int(input()) for _ in range(M)]

start, end = 1, max(bosuk)
while start <= end:
    mid = (start + end) // 2

    cur = 0 
    for i in range(M):
        cur += bosuk[i] // mid
        if bosuk[i] % mid !=0:
            cur += 1

    if cur > N:
        start = mid + 1
    else:
        res = mid
        end = mid - 1

print(res)
'''
11:59~~12:40 (41m) 이분 탐색 조건을 뭘로 설정해야할지 모르겠음
    (전체 보석 수 // 아이들 수) 값을 차례로 분배하는 방법밖에 생각이 안난다
    
~52 (12m) 풀이 참고
    start는 mid값이 0이 되는 것을 막기 위해 1로 세팅. end는 맞음
    이분 탐색 조건 변수 :: "보석을 받을 수 있는 아이들 수"
    
결국 처음 생각했던 '(전체 보석 수 // 아이들 수) 값을 차례로 분배하는 방법밖에 생각이 안난다' 이게 맞았다
여기서 어떻게 조금 더 생각했어야 했나?
    bosuk[i]%mid는 mid보다 클 수가 없음
    이렇게 남는게 발생한다면 1명으로 카운트를 해준다
    기존에 어떤 보석을 받았는지 고려해줄 필요가 없음
    -> 이렇게 계산한 값이 아이들 수보다 크면, 각 아이들에게 줄 보석 수를 늘림
    
**탐색 변수를 어떻게 정의해야 될 지 모르겠을 땐, 주어진 변수와 비교해 보는 것을 한번 생각해보기**
'''