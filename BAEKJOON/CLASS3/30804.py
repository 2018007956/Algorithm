# 풀이 공부
import sys
input = sys.stdin.readline
from collections import defaultdict

def solution():
    max_length = 0
    cnt = defaultdict(int)
    unique_cnt = 0

    s = 0 # 시작 포인터
    for e in range(N): # 끝 포인터
        cnt[tang[e]] += 1 # 끝 포인터가 가리키는 숫자의 개수를 증가시킴
        if cnt[tang[e]] == 1: 
            unique_cnt += 1 # 새로운 숫자가 추가되면 고유 숫자 개수 증가
        
        # 고유 숫자 개수가 2를 초과하면 윈도우의 앞 부분을 줄임
        while unique_cnt > 2:
            cnt[tang[s]] -= 1
            if cnt[tang[s]] == 0:
                unique_cnt -= 1 # 고유 숫자가 제거되면 고유 숫자 개수 감소
            s += 1 # 윈도우의 시작 포인터를 오른쪽으로 이동

        # 현재 윈도우의 길이를 계산하고 최대 길이 갱신
        max_length = max(max_length, e-s+1)
        
    return max_length
    

N = int(input())
tang = list(map(int, input().split()))
print(solution())

'''
11:31~36, 5:30~52 (27m) 시간 초과
    slicing 많이 써서 그런듯

import sys
input = sys.stdin.readline

def solution():
    s, e = 0, N
    left = True
    while s <= e:
        if len(set(tang[s:e]))<=2:
            return e-s
        if tang[s]==tang[e-1]: ## 같은 경우 어떻게 처리? 양 끝 없애가면서 먼저 다른 숫자가 나오는 쪽 찾아서 반대편부터 없애기
            tmps, tmpe = s, e
            check_num = 0
            while tmps <= tmpe:
                if tang[tmps]==tang[tmpe-1]:
                    check_num = tang[tmps]
                    tmps += 1
                    tmpe -= 1
                else:
                    if check_num == tang[tmps]:
                        left = False       
                    break   
        
        if set(tang[s+1:e]) < set(tang[s:e-1]):
            s += 1
        elif set(tang[s+1:e]) > set(tang[s:e-1]):
            e -= 1 
        else:
            if left:
                s += 1
            else:
                e -= 1

N = int(input())
tang = list(map(int, input().split()))
print(solution())

시간 초과 나는 이유 (by GPT) : set을 사용해서 부분 배열의 중복을 제거하고 그 길이를 확인하는 과정에서 O(N)이 여러 번 반복됨 -> 비효율적
해결법 : 투포인터 사용
tang = [1 1 2 1 5] 와 같이 5가 빠져야 되는 경우도, 
max_lengh을 갱신해주는 방식으로 동작하기 때문에 5가 들어오기 전에 길이 4 ([1,1,2,1]) 로 갱신됨  
'''