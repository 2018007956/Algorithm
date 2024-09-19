# Solved (58m)
def rotate(num, dir):
    # 시계 방향 회전
    if dir == 1: 
        topni[num] = topni[num][-1] + topni[num][:-1]
    # 반시계 방향 회전
    else:
        topni[num] = topni[num][1:] + topni[num][0]


topni = [input() for _ in range(4)]

K = int(input())
for _ in range(K):
    num, dir = map(int, input().split())
    num -= 1
    topni_base = topni[:]
    rotate(num, dir)

    prev_left_isrotate = True
    prev_right_isrotate = True
    for i in range(1, 4):
        if i%2==1:
            if prev_left_isrotate and 0<=num-i<4 and topni_base[num-i][2] != topni_base[num-i+1][-2]:
                rotate(num-i, -dir)
            else:
                prev_left_isrotate = False
            if prev_right_isrotate and 0<=num+i<4 and topni_base[num+i][-2] != topni_base[num+i-1][2]:
                rotate(num+i, -dir)
            else:
                prev_right_isrotate = False
        else:
            if prev_left_isrotate and 0<=num-i<4 and topni_base[num-i][2] != topni_base[num-i+1][-2]:
                rotate(num-i, dir)
            else:
                prev_left_isrotate = False
            if prev_right_isrotate and 0<=num+i<4 and topni_base[num+i][-2] != topni_base[num+i-1][2]:
                rotate(num+i, dir)
            else:
                prev_right_isrotate = False
                
score = 0
for i, x in enumerate(topni):
    score += int(x[0]) * (2**i)
print(score)