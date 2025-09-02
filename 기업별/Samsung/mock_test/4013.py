# Solved
T = int(input())
for test_case in range(1, T + 1):
    k = int(input())
    magnetics = [list(map(int, input().split(' '))) for _ in range(4)]

    for _ in range(k):
        m_num, r_dir = tuple(map(int, input().split()))
        m_num -= 1
        # 현재 자석 회전
        if r_dir == 1:
            tmp = magnetics[m_num][-1]
            magnetics[m_num] = [tmp] + magnetics[m_num][:-1]
        else:
            tmp = magnetics[m_num][0]
            magnetics[m_num] = magnetics[m_num][1:] + [tmp]

        # 왼쪽 체크
        left_chk_num = m_num
        left_chk_dir = r_dir
        while left_chk_num >= 1:
            if left_chk_dir == 1 and magnetics[left_chk_num][7] != magnetics[left_chk_num-1][2]: # 시계 (회전 전 정보로 판단해야 함)
                # 왼쪽은 반시계 회전 
                tmp = magnetics[left_chk_num-1][0]
                magnetics[left_chk_num-1] = magnetics[left_chk_num-1][1:] + [tmp]
            elif left_chk_dir == -1 and magnetics[left_chk_num][5] != magnetics[left_chk_num-1][2]: # 반시계
                tmp = magnetics[left_chk_num-1][-1]
                magnetics[left_chk_num-1] = [tmp] + magnetics[left_chk_num-1][:-1] 
            else:
                break

            left_chk_num -= 1
            left_chk_dir *= -1
        
        # 오른쪽 체크
        right_chk_num = m_num
        right_chk_dir = r_dir
        while right_chk_num<=2:
            if right_chk_dir == 1 and magnetics[right_chk_num][3] != magnetics[right_chk_num+1][6]:
                tmp = magnetics[right_chk_num+1][0]
                magnetics[right_chk_num+1] = magnetics[right_chk_num+1][1:] + [tmp]
            elif right_chk_dir == -1 and magnetics[right_chk_num][1] != magnetics[right_chk_num+1][6]:
                tmp = magnetics[right_chk_num+1][-1]
                magnetics[right_chk_num+1] = [tmp] + magnetics[right_chk_num+1][:-1]
            else:
                break

            right_chk_num += 1
            right_chk_dir *= -1


    score = 0
    for i in range(4):
        score += magnetics[i][0] * (2**i)
    print(f'#{test_case} {score}')


# 다른 풀이 : DFS
def dfs(num, dir):
    global check
    check[num] = 1
    if num < 3:
        if mag[num][2] != mag[num+1][6] and not check[num+1]:
            dfs(num+1, -1*dir)
    if num > 0:
        if mag[num][6] != mag[num-1][2] and not check[num-1]:
            dfs(num-1, -1*dir)

    if dir == 1:
        mag[num] = [mag[num].pop()] + mag[num]
    else:
        mag[num] = mag[num][1:] + [mag[num][0]]

T = int(input())
for tc in range(1, T+1):
    k = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(k):
        n, d = map(int, input().split())
        check = [0]*4
        dfs(n-1, d)

    res = 0
    for i in range(4):
        res += mag[i][0] * 2 ** i
    print(f'#{tc} {res}')