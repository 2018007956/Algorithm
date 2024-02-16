import sys
from collections import Counter
N, M, B = map(int, input().split())
ground = []
for i in range(N):
    ground.extend(list(map(int, sys.stdin.readline().split())))

def cal_time(ground, value, B):
    time = 0
    if value>256 or value<0:
        return 9999, 0

    for i in ground:
        if i > value: # remove block: 2sec
            time += 2 *(i-value)
            B += i-value
        elif i < value: # put block: 1sec
            time += 1*(value-i)
            B -= value-i
    # 가지고 있는 블록보다 많이 쓴 경우는 B>0이 될 때까지 높은 층부터 한 층 씩 block제거
    # pre_time = time
    # while B < 0:
    #     value -= 1
    #     remove_block_cnt = ground.count(max(ground))
    #     B += remove_block_cnt
    #     time += 2*remove_block_cnt
    #     ground = [x-1 for x in ground if x==max(ground)] # ground update
    #     if value<0:
    #         return 9999, 0
    #     return time - pre_time, value
    return time, value


# mean = cal_time(ground, int(round(sum(ground)/len(ground))), B)
# mode = cal_time(ground, Counter(ground).most_common()[0][0], B)
# print(int(round(sum(ground)/len(ground))), Counter(ground).most_common()[0][0])
# print(mean, mode)

res_min = cal_time(ground, min(ground), B)
for x in range(min(ground)+1, max(ground)+1):
    res = cal_time(ground, x, B)
    if res[0]<res_min[0] or (res[0]==res_min[0] and res[1]>res_min[1]):
        res_min = res
print(*res)


'''
# 경우의 수:
# 1. 평균값으로 맞추는 경우
# 2. 최빈값으로 맞추는 경우
# 3. 인벤토리가 비어있어 put을 못하는 경우


반례1)
1 3 68
0 0 1
정답: 2 1
내답: 2 0
-> 내가 나눈 두 경우의 수 모두 해당 안됨 
-> 저 두가지만 하는게 아니라 min 부터 max까지 다 돌려야 할듯
그리고 조건 반영 안됨: 답이 여러개 일 시 땅 높이가 높은 것 출력

반례2)
3 4 11
29 51 54 44
22 44 32 62
25 38 16 2
정답: 250 35
내답: 2 43

반례3)
4 4 36
15 43 61 21
19 33 31 55
48 63 1 30
31 28 3 8
정답: 355 32
내답: 357 31

반례4)
2 2 0
256 256
0 0
정답: 768 128
내답: 4 255

반례4)
7 7 6000
30 21 48 55 1 1 4
0 0 0 0 0 0 0
15 4 4 4 4 4 8
20 40 60 10 20 30 2
1 1 1 1 1 1 9
24 12 33 7 14 25 3
3 3 3 3 3 3 32
정답: 879 10
내답: 881 12

반례5)
2 2 35
20 10
190 40
정답: 350 40
내답: 375 65

반례6)
2 2 68
120 90
250 170
정답: 290 170
내답: 314 158
'''