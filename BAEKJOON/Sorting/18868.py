# 18868
# Solved (39m)
M, N = map(int, input().split())
space = []
for _ in range(M):
    s = {}
    cnt = 1
    for i in list(map(int, input().split())):
        s[i] = cnt
        cnt += 1
    
    s = dict(sorted(s.items()))
    space.append(list(s.values()))

ans = 0
for i in range(M-1):
    for j in range(i+1, M):
        if space[i]==space[j]:
            ans += 1
print(ans)
'''
9:24~44 (20m) 틀렸습니다
    순서 같은 경우가 3개 있다면 -> 3쌍인데, 
    len(space)-len(set([tuple(x) for x in space])) 이 방식으론 2개로 나옴

~10:03 (19m) Solved
'''

## 조금 더 정리된 코드 by GPT 
M, N = map(int, input().split())
space = []
for _ in range(M):
    coords = list(map(int, input().split()))
    ## 틀린 코드 
    # sorted_coords = sorted(enumerate(coords), key=lambda x: x[1])
    # normalized = [index + 1 for index, _ in sorted_coords] 
    ## 정답 코드
    rank = {value: i+1 for i, value in enumerate(sorted(coords))}
    normalized = [rank[value] for value in coords]
    space.append(tuple(normalized))

ans = 0
for i in range(M-1):
    for j in range(i+1, M):
        if space[i]==space[j]:
            ans += 1
print(ans)
'''
97% 틀렸습니다
    대부분 다 통과하는거면 엣지케이스를 생각해보자
    같은 값 처리해주는 부분에서 에러 발생?
반례
2 4
1 2 2 3
1 1 2 3
[정답] 0
[출력] 1
내 코드는 index 정보를 집합으로 다루기 때문에, 동일 값이 있는 경우 뒤쪽 index로 저장되는 반면
GPT 코드는 같은 값도 서로 다른 index로 처리하기 때문에 위와 같은 경우를 같은 쌍으로 판단하게 된다

~10:34 (30m) Solved

알게된 점 : 정렬할 때 enumerate로 index값을 사용하면 간편하게 순서를 고려해줄 수 있음
'''