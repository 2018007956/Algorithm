#26107 - 시간초과
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
interval = [[]]
for i in range(1,n+2):
    if i==n+1:
        visit = list(map(int, input().split()))
        break
    a, b = map(int, input().split())
    # interval: [number], start, end
    interval.append(([i],a,b))

num = 1
while True:
    # 종료 조건 (num이 조건에 의해 +되기 때문에 ==말고 부등호로 종료조건 넣어야) 
    if num>=len(interval)-2:
        break 

    # 두 interval의 교차된 끝점 차이가 <<이거나 >> 인경우
    print(interval)
    if (interval[num+1][1]-interval[num][2])>0 and  (interval[num+1][2]-interval[num][1])>0 \
        or (interval[num+1][1]-interval[num][2])<0 and  (interval[num+1][2]-interval[num][1])<0:
        num += 1
        pass
    
    # num과 num+1번째 interval은 겹치기 때문에 num으로 합쳐줌, num+1은 제거
    right = max(interval[num][2], interval[num+1][2])
    left = min(interval[num][1], interval[num+1][1])
    interval[num] = (interval[num][0]+interval[num+1][0],left, right)
    # interval.pop(num+1) # -> 이게 시간 걸리는건가?


    
# Calculate distance in advance
dist = [0, 0]
prefix_sum = 0
for i in range(2,len(interval)):
    prefix_sum += interval[i][1]-interval[i-1][2]
    dist.append(prefix_sum)
print('dist',dist)

total_dist = 0
current_group = 1
for pos in visit:
    # find group index in list interval
    group = 1
    for r in interval[1:]:
        if pos <= r[0][-1]:
            break
        group += 1
        
    if current_group == group:
        pass
    else:
        if current_group < group:
            total_dist += dist[group]-dist[current_group]
        else:
            total_dist += dist[current_group]-dist[group]
    print('pos-group-total_dist',pos, group,total_dist)
    current_group = group

print(total_dist)



'''
Dict 구현시 문제점
{1: (0, 3), 2: (0, 3), 3: (3, 5), 4: (6, 7)}
{1: (0, 3), 2: (0, 5), 3: (0, 5), 4: (6, 7)}
앞뒤만 비교해서 값이 바뀌기 떄문에, 1까지 (0, 5)로 바껴야 되는데 안바뀜

리스트로 키를 합치도록 구현하면 아래와 같이 나옴
문제는 여기서 어떻게 탐색할 것인가
[[], ([1, 2], 0, 3), ([3], 3, 5), ([4], 6, 7)]
[[], ([1, 2, 3], 0, 5), ([4], 6, 7)]
번호가 여러개인 경우 펼치기..!
# # 번호 펼치기 
# new_interval = [[]]
# for i in range(1,len(interval)):
#     if len(interval[i][0])>1:
#         for j in interval[i][0]:
#             new_interval.append((interval[i][1],interval[i][2]))
#     else:
#         new_interval.append((interval[i][1],interval[i][2]))
# print(new_interval)

또 다르 문제점 발견: 출발지와 목적지 사이에 또다른 interval이 있는 경우
-> 펼치지 말고 그룹화 시켜서 보는게 편하긴 한데..
구현 아이디어: 각 interval의 시작지점만 모아놓은 리스트를 활용하여
visit number가 리스트의 어떤 수보다 큰지 확인하여 interval 값 파악

결과: 시간초과 -> 원인: 누적합 문제
** 가운데 interval 길이 계산은 distance를 미리 누적합으로 구해놓고 사용하면 일일이 안빼줘도 됨!
# # Think middle group -> 필요없음
# if group - current_group>=2:
#     for x in range(current_group+1,group):
#         total_dist -= interval[x][2]-interval[x][1]
 
결과: 시간초과 -> 원인: pop(index)하는데 시간 걸린다고 추측 -> pop 없이 구현

'''