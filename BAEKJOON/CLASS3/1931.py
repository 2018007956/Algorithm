# Solved (42m)
N = int(input())
meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append([s, e])

meetings.sort(key = lambda x:(x[1], x[0]))

cnt = 0
start, end = 0, 0
for s, e in meetings:
    if end <= s:
        end = e
        cnt += 1

print(cnt)

'''
8:52~9:24 (32m) 
어떻게 처리해줘야 할지 감이 안잡힘
start time이 작은 순서대로 돌면서 카운트, 더 작은 범위로 포함되면 그 값을 기준값으로 update 하는 방식으로 구현
75?80%까지 되다가 틀렸습니다 뜸

~9:34 (10m)
**end, start 순으로 정렬** -> 포함되는 범위 생각 안해줘도 됨, 아래 코드 제거
elif start <= s and e <= end: # 작은 범위로 update
    start = s
    end = e    
'''