N = int(input())

for num in range(1, N):
    constructor = num + sum([int(str(num)[i]) for i in range(len(str(num)))])
    if constructor == N:
        print(num)
        break
else:
    print(0)

'''
N의 분해합: N과 N을 이루는 각 자리수의 합
245의 분해합: 245+2+4+5=256
245는 256의 생성자

분해합: 216
생성자: ? 198+11+9+8=216
int(x) + sum([int(x[i]) for i in range(len(x))]) == N인 x찾기     
Bruth force로 x값 하나씩 올리면서 해봤는데 시간 초과 될듯
엥 시간 초과 안되네 ㅇㅁㅇ
아 범위를 1,000,000까지가 아니라 N까지 하면 됨
'''