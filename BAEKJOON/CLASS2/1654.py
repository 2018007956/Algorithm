# Solved in 57m (w/ search..)
K, N = map(int, input().split())

line = []
for _ in range(K):
    line.append(int(input()))
    
start = 1
end = max(line)
while start <= end:
    max_len = (start+end)//2
    
    cnt = 0
    for num in line:
        cnt+=num//max_len

    if cnt >= N: # 최대 길이 연장 가능
        start = max_len + 1
    else: # 최대 길이 줄여야 됨
        end = max_len - 1
        
print(end) # 최대 랜선 길이를 구해야 하므로 end 출력

'''
6:18~6:38 (20m) 
어떻게 풀어야할지 감이 안잡힘 
힌트를 얻어 이분탐색으로 풀어보는중 

11:10~11:47 (37m)
매개 변수 탐색 예제 공부 (https://velog.io/@qazws78941/python%EB%A7%A4%EA%B0%9C-%EB%B3%80%EC%88%98-%ED%83%90%EC%83%89)
이분 탐색 조건을 처음에 잘못 설정해줬다. 기준을 전선 개수(cnt)와 N의 비교로 했어야 하는데
max_len*N <= sum(line) 이걸 검토하며 이분탐색 하니까 cnt==N인 경우가 답으로 안나왔던 것.
'''