# Solved (48m)
x, y = map(int, input().split())

Z = (y*100)//x
if Z>=99:
    print(-1)

else:
    start, end = 0, x
    while start <= end:
        mid = (start + end) // 2

        if (y+mid)*100//(x+mid) > Z:
            end = mid - 1
        else:
            start = mid + 1

    print(start)

'''
10:28~52 (24m) 4% 틀렸습니다
    승률이 변하지 않는 조건 : Z >=99%
        승률이 100%가 되기 위해서는 모든 게임에서 승리해야 하는데,
        몇 번을 더 이겨도 소수점 이하는 버리기 때문에 여전히 99%에 머무르게 됨

4$ 틀렸습니다
    파이썬 부동소수점 문제
    int(y/x*100)을 int(y*100/x)이나 (y*100)//x로 바꾸니 정답
'''