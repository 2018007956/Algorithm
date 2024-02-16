N, M, K = map(int, input().split())

board = []
for i in range(N):
    board.append(list(input()))

Q = input()
round = []
calculate = [[0 for j in range(M)] for i in range(N)]
for i in range(int(Q)):
    tmp = list(map(int, input().split()))
    round.append(tmp)
    if '#' in tmp:


for x, y in round: # start pos
    while True:
        calculate[x+K,y+K]
        if K==0:



'''
for x, y in round:
    while True:
        x+=K
        y+=K
        if K==0:
            x+=1 or y+=1 -> 두가지 경우를 어떻게 다 고려하지?
            말을 기준으로 생각하는게 아니라 칸을 기준으로 미니멈값 구해놓고
            어떤 턴에 도착하는지만 알면됨
'''