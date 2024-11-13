# 풀이 공부
import sys
import math
input = sys.stdin.readline
def room(max_hp):
    cur_hp = max_hp
    cur_atk = Hatk

    for t, a, h in rooms:
        # 몬스터 방
        if t==1:
            # 몬스터를 몇 번 공격해야 문스터가 죽는지
            monster_hits = math.ceil(h / cur_atk)
            # 몬스터가 주인공을 몇 번 공격할 수 있는지
            hero_hits = monster_hits - 1 # 몬스터는 주인공이 죽지 않을 때만 공격함

            cur_hp -= hero_hits * a
            if cur_hp <= 0:
                return False

        # 포션 방
        elif t==2:
            cur_atk += a
            cur_hp = min(max_hp, cur_hp + h)
    
    return True        


N, Hatk = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

start, end = 0, int(1e18) # 주인공의 체력 범위
answer = end
while start <= end:
    mid = (start + end) // 2
    if room(mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
'''
이분탐색을 한번 수행할 때마다 전체 방을 다 돈다
중간에 죽으면 start를 높이고, 끝까지 살아 남으면 end를 줄임
'''