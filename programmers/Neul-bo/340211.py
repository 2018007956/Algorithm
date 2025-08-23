from collections import defaultdict, Counter
def solution(points, routes):
    
    move = defaultdict(list)
    for i in range(len(routes)):  
        t = 0
        for j in range(len(routes[i])-1): 
            start_x, start_y = points[routes[i][j]-1]
            dest_x, dest_y = points[routes[i][j+1]-1]

            move_r, move_c = dest_x-start_x, dest_y-start_y
            while abs(move_r):
                move[t].append((start_x, start_y))
                t += 1
                if move_r > 0:
                    start_x += 1
                    move_r -= 1
                else:
                    start_x -= 1
                    move_r += 1
                    
            while abs(move_c):
                move[t].append((start_x, start_y))
                t += 1
                if move_c > 0:
                    start_y += 1
                    move_c -= 1
                else:
                    start_y -= 1
                    move_c += 1
                    
            # 도착 좌표 기록은 '마지막 구간'에서만 1번
            if j==len(routes[i])-2:
                move[t].append((start_x, start_y))
            
    answer = 0 
    for i in range(len(move)):
        answer += len([x for x in Counter(move[i]).values() if x>1])
            
    return answer

'''오답노트
1. for j in range(len(routes[0])-1): -> for j in range(len(routes[i])-1)
    모든 로봇의 경로 길이가 같다는 보장이 없음
2. 구간 전환 때 “같은 시간 t에 같은 좌표를 두 번 기록”
    각 구간(j→j+1) 이동을 마칠 때 move[t].append((start_x, start_y))로 도착 좌표를 한 번 기록하고, 
    다음 구간을 시작하자마자 while의 첫 줄에서 같은 시각 t에 같은 좌표를 또 넣고 있음
    이러면 “로봇 1대”가 한 시각에 동일 좌표를 2번 기록해버려 충돌로 잘못 집계될 수 있음
    도착 좌표는 “마지막 구간에서만” 한 번 넣도록 바꿔야 함
'''