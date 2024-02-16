N = int(input())
p = []
for i in range(N):
    weight, height = map(int, input().split())
    p.append([weight,height])

for i in p:
    rank = 1
    for j in p:
        if i[0]<j[0] and i[1]<j[1]:
            rank += 1
    print(rank, end = ' ')

'''
w: [[2, 88], [3, 60], [1, 58], [0, 55], [4, 46]]
h: [[2, 186], [0, 185], [1, 183], [3, 175], [4, 155]]
       1         2          2         2         5
2중for문 돌면서 rank 카운트 함
w을 기준으로 잡으면, w[0]값과 같은 값이 나올 때까지 같은 등수 유지하며 카운트

5
55 185
58 175
88 186
60 183
46 155
w: [[2, 88], [3, 60], [1, 58], [0, 55], [4, 46]]
h: [[2, 186], [0, 185], [3, 183], [1, 175], [4, 155]]
       1         2           2        3         4
       1         2           2        2         3
위와 같은 경우도 있으므로
h를 기준으로도 한번 돌려보고 작은 숫자 출력

N = int(input())
w, h = [],[]
for i in range(N):
    weight, height = map(int, input().split())
    w.append([i, weight])
    h.append([i, height])

w.sort(key=lambda x:x[1],reverse=True)
h.sort(key=lambda x:x[1],reverse=True)
# print(w)
# print(h)

# w 기준으로 등수 매기기
rank = 1
for i in w:
    cnt = 0
    for j in h:
        if len(j)!=3:
            j.append(rank)
            cnt += 1
            if i[0] == j[0]:
                rank += cnt
                break

# h 기준으로 등수 매기기
rank = 1
for i in h:
    cnt = 0
    for j in w:
        if len(j)!=3:
            j.append(rank)
            cnt += 1
            if i[0] == j[0]:
                rank += cnt
                break

h.sort(key=lambda x:x[0])
w.sort(key=lambda x:x[0])
for i,j in zip(w,h):
    if i[2] < j[2]:
        print(i[2], end = ' ')
    else:
        print(j[2], end = ' ')

sort를 너무 많이 해서 시간초과 뜰 것 같은 느낌
. . . 결과) 틀림
-> 기존 list에 rank를 넣으면서 센다는게 너무 복잡하고 비효율적

복잡해질수록 간단하게 생각!

문제를 다시 읽어보면:
N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람 수로 정해진다
-> 자기보다 크고 무거운(둘 다 큰) 사람이 몇 명인지 쟤서 자기 등수만 정하면 된다
'''