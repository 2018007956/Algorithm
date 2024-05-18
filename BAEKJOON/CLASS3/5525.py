N = int(input())
M = int(input()) # len of S
S = input()

# Make Pn
P = 'I' + 'OI'*N
# Count how many Pn in S
cnt = 0
check = 0
i = 0
while i < M:
    if S[i:i+3]=='IOI':
        check += 1
        if check==N:
            cnt += 1
            check -= 1
        i += 2
    else: # 연속하지 않는 경우
        check = 0
        i += 1
print(cnt)

'''
print('OOIOIOIOIIOII'.count('IOI')) -> 3 -> 겹치는게 안세지므로 

S[i:i+len(P)]==P
50점, 테스트2 시간 초과
Ref) https://aia1235.tistory.com/30
파이썬에서 arr[a:b]의 시간 복잡도는 O(b-a)이다
서브테스크 2는 1000000(N) * 1000000(M) 이기 때문에 시간 초과
슬라이스를 최대한 덜 쓰고 반복을 최소화하는 방법 생각해보기

S[i:i+3]=='IOI'
Pn이 IO가 반복되는 구조이므로 IOI만을 비교해보자
4% 틀렸습니다
for 문으로 i가 하나씩 늘어나는 방식이 아니라
이어지지 않는 경우, IOI맞는 경우 다루기 위해 while문으로 커서 이동하는 방식으로 구현
'''