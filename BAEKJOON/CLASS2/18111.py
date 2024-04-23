# 2024-04-23
def calculate(height):
    inventory = B
    flag = False
    time_cnt = 0
    for i in range(len(ground)):
        if ground[i] > height: # Remove block (2s)
            diff = ground[i] - height
            time_cnt += 2*diff
            inventory += 1*diff
        elif ground[i] < height: # Insert block (1s)
            diff = height - ground[i]
            time_cnt += 1*diff
            inventory -= 1*diff
            if inventory < 0:  # 인벤토리에 블록 부족 -> 높이 재설정 필요
                flag = True 
                break
        else:
            continue
    return time_cnt, flag

N, M, B = map(int, input().split())
ground = []
for i in range(N):
    ground.extend(list(map(int, input().split())))

g_set = set(ground)
best_time, result_height = 1e8, 0
for height in range(min(g_set), max(g_set)+1):
    time_cnt, flag = calculate(height)
    if not flag and time_cnt <= best_time:
        best_time = time_cnt
        result_height = height
print(best_time, result_height)


# from collections import Counter
# candidate = []
# # 주어진 height 내에서 빈도수 순서대로 검토
# counter = Counter(ground)
# counter = sorted(counter.items(), key=lambda x:(-x[1],-x[0])) # -: 내림차순

# reset = False
# for k in range(len(counter)):
#     height = counter[k][0]
#     time_cnt, flag = calculate(height)
#     if not flag: # if flag : # 1 more round
#         break

# candidate.append([time_cnt, height])
# 평균값 candidate 도 계산 후 best 값 추출
# result_time, result_height = sorted(candidate)[0]
# print(result_time, result_height)

'''
# 4:38~5:22 (44m) 틀림

문제 조건 중 
'땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다'
이 조건을 고려해주지 않았음
=> 어차피 주어지는 값 중에서 height를 정하기 때문에 256 보다 크게 설정될 수 없음
=> 이게 문제였다 
중간값, 평균값을 height으로 설정할 때 더 적은 시간이 걸릴 수 있음을 간과

# 5:24~5:43 (20m) 
평균값 고려해줬지만 틀림

# 5:49~5:57 (8m)
뭐가 문제일까?
평균값이 아니라 가능한 모든 height값 (0~256) 돌려보기
=> 시간초과
    for문 안에서 함수를 호출하는데 그 함수 내에 for문이 구현되어 있어, 2중 포문 구조이므로 시간초과 
=> 값의 범위를 좁혀야 하지 않을까/ 최빈값, 평균값 외에 어떤 값이 될 수 있지? 

# 6:08~6:33 (25m)
candidate 으로 결과값 다 받는 구조를 변수에 best 값 업데이트 하는 방식으로 바꿈
=> 시간초과
게시판에서 반례 발견
2 2 0
1 1
1 5
[정담] 8 1
[출력] 2 1
같은 위치에서 블록을 여러 개 제거해 주는 경우 고려 안함
=> diff 변수 추가
가능한 height 범위를 평균값이 아니라 min~max까지 돌려봐야 할듯
평균값만이 best time을 갖는 height일거라는 근거가 없음
=> 시간초과

::: 시간초과 뜨는 이유 분석해보기 :::
'''










# 2023-01-11
# import sys
# from collections import Counter
# N, M, B = map(int, input().split())
# ground = []
# for i in range(N):
#     ground.extend(list(map(int, sys.stdin.readline().split())))

# def cal_time(ground, value, B):
#     time = 0
#     if value>256 or value<0:
#         return 9999, 0

#     for i in ground:
#         if i > value: # remove block: 2sec
#             time += 2 *(i-value)
#             B += i-value
#         elif i < value: # put block: 1sec
#             time += 1*(value-i)
#             B -= value-i
#     # 가지고 있는 블록보다 많이 쓴 경우는 B>0이 될 때까지 높은 층부터 한 층 씩 block제거
#     # pre_time = time
#     # while B < 0:
#     #     value -= 1
#     #     remove_block_cnt = ground.count(max(ground))
#     #     B += remove_block_cnt
#     #     time += 2*remove_block_cnt
#     #     ground = [x-1 for x in ground if x==max(ground)] # ground update
#     #     if value<0:
#     #         return 9999, 0
#     #     return time - pre_time, value
#     return time, value


# # mean = cal_time(ground, int(round(sum(ground)/len(ground))), B)
# # mode = cal_time(ground, Counter(ground).most_common()[0][0], B)
# # print(int(round(sum(ground)/len(ground))), Counter(ground).most_common()[0][0])
# # print(mean, mode)

# res_min = cal_time(ground, min(ground), B)
# for x in range(min(ground)+1, max(ground)+1):
#     res = cal_time(ground, x, B)
#     if res[0]<res_min[0] or (res[0]==res_min[0] and res[1]>res_min[1]):
#         res_min = res
# print(*res)


# '''
# # 경우의 수:
# # 1. 평균값으로 맞추는 경우
# # 2. 최빈값으로 맞추는 경우
# # 3. 인벤토리가 비어있어 put을 못하는 경우


# 반례1)
# 1 3 68
# 0 0 1
# 정답: 2 1
# 내답: 2 0
# -> 내가 나눈 두 경우의 수 모두 해당 안됨 
# -> 저 두가지만 하는게 아니라 min 부터 max까지 다 돌려야 할듯
# 그리고 조건 반영 안됨: 답이 여러개 일 시 땅 높이가 높은 것 출력

# 반례2)
# 3 4 11
# 29 51 54 44
# 22 44 32 62
# 25 38 16 2
# 정답: 250 35
# 내답: 2 43

# 반례3)
# 4 4 36
# 15 43 61 21
# 19 33 31 55
# 48 63 1 30
# 31 28 3 8
# 정답: 355 32
# 내답: 357 31

# 반례4)
# 2 2 0
# 256 256
# 0 0
# 정답: 768 128
# 내답: 4 255

# 반례4)
# 7 7 6000
# 30 21 48 55 1 1 4
# 0 0 0 0 0 0 0
# 15 4 4 4 4 4 8
# 20 40 60 10 20 30 2
# 1 1 1 1 1 1 9
# 24 12 33 7 14 25 3
# 3 3 3 3 3 3 32
# 정답: 879 10
# 내답: 881 12

# 반례5)
# 2 2 35
# 20 10
# 190 40
# 정답: 350 40
# 내답: 375 65

# 반례6)
# 2 2 68
# 120 90
# 250 170
# 정답: 290 170
# 내답: 314 158
# '''