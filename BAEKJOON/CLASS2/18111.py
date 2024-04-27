# 2024-04-23 (3h 47m) TLE Solved
import sys
from collections import Counter
input = sys.stdin.readline

def calculate(height):
    inventory = B
    flag = False
    time_cnt = 0
    for h, c in counter:
        if h > height: # Remove block (2s)
            diff = h - height
            time_cnt += 2*diff * c
            inventory += 1*diff * c
        else:   # h < height: # Insert block (1s)
            diff = height - h
            time_cnt += 1*diff * c
            inventory -= 1*diff * c
            if inventory < 0:  # 인벤토리에 블록 부족 -> 높이 재설정 필요
                flag = True 
                break
    return time_cnt, flag

N, M, B = map(int, input().split())
ground = []
for i in range(N):
    ground.extend(list(map(int, input().split())))

counter = Counter(ground) # O(N)
counter = sorted(counter.items(),reverse=True) # 내림차순 O(NlogN)
best_time, result_height = 1e8, 0
for height in range(min(ground), max(ground)+1):
    time_cnt, flag = calculate(height)
    if not flag and time_cnt <= best_time:
        best_time = time_cnt
        result_height = height
print(best_time, result_height)

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
  값의 범위를 좁혀야 하지 않을까/ 최빈값, 평균값 외에 어떤 값이 될 수 있지? 
>> ground에 존재하는 값들, 그리고 그 평균값만을 가능한 height로 지정해준다는 것에 있어 근거가 없음
>> ground에 존재하는 min값부터 max값까지 모든 값을 다 시도해 봐야함

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
12:10~1:50 (1h 40m)
B에는 최대 500*500*256 = 64,000,000 = 6.4*10^7 개의 블록 존재 가능
=> 대략 10^8(1억)번은 1초정도 걸리므로 브루트포스로 풀어도 시간 제한 안에 해결 가능
=> 2중 포문 불가 >> counter가 모두 다른 값을 가지고 있는 최악의 경우 6.4*10^7 * 256 = 약 1.6*10^10 이므로 시간 초과 되야하는거 아닌가?
=> 질문 게시판 글 올림 : https://www.acmicpc.net/board/view/141727
==> input이 500*500인거지 코드를 돌아가는 구조를 분석하면 257^2회가 되어서 넉넉하게 돌아감!

(PyPy3으로 제출하면 시간초과 안뜬다는 사례도 많아서 해봤는데 틀렸습니다 뜸)
참고한 풀이 : https://dawitblog.tistory.com/72
ground 값 하나씩 다 돌지 않고, set으로 묶은 다음 개수만큼 개산해 줄 수 있을 듯
for i in range(len(ground)) -> for h, c in counter.items()
=> 틀렸습니다

반례 모음집에서 찾아봤다
2 2 35
20 10
190 40
[정답] 350 40
[출력] 366 32
>> calculate의 조건문 순서!!
>> height가 높은게 먼저오도록 내림차순 정렬하여 inventory 주머니를 먼저 늘리는 것도 필요
>> 다른 블록을 활용하여 쌓을 수 있는데 먼저 Insert 하다가 flag=True 되버리면 안됨!!! <<
=> 시간 초과 (PyPy3로 해도 시간초과)
else와 elif의 시간 차이가 많이 난다고 하여 (https://ggodong.tistory.com/297)
else로 수정했지만 시간초과 그대로 발생
=> 근데 위 참고 사이트에 나온 코드가 내 코드랑 완전 똑같이 구현되어 있는데, 나만 시간초과 뜨는 이유가 뭘까..

3:20~50 (30m)
counter 계산 및 sorted를 caculate 함수 안에서 해줄 필요가 없음
=> 이 부분 수정해주니까 pypy3 성공
Python으로 하니까 더 빠르고 적은 메모리 사용해서 성공
'''