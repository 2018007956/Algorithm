# Solved (35m)
import sys
input = sys.stdin.readline

def binary_search():
    snack.sort()

    start = 1
    end = snack[-1]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        
        cnt = 0
        for i in range(N):
            cnt += snack[i] // mid
                
        # 과자가 아이들 수보다 부족한 경우, 과자 길이 줄이기
        if cnt < M: 
            end = mid - 1
        # 과자가 남는 경우, 과자 길이 늘리기
        else:
            result = mid
            start = mid + 1
    
    print(result)

M, N = map(int, input().split())
snack = list(map(int, input().split()))
binary_search()

'''
3:36~42, 46~4:05 (25m) 시간초과
    snack_copy = snack[:]
    for i in range(N-1, -1, -1):
        while snack_copy[i] >= mid:
            snack_copy[i] -= mid
            cnt += 1
    위 부분이 시간 많이 걸릴 것이라 생각
    나눠서 몫을 구하는 방식으로 수정

~09 (4m) python 1% 시간 초과 pypy 시간 초과

9:41~47 (6m) Solved
    end -= 1이 아니라 end -= mid-1로 줄여야 탐색 범위가 절반으로 줄어들어 효율적인 탐색 가능
    그리고 아래와 같이 구현하면 최대값이 아닌데 출력될 수 있음
    if cnt == M:
        print(mid)
        break
'''