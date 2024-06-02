# Solved (11m)
def dac(a, b, c):
    if b==1:
        return a%c
    elif b%2==0:
        return dac(a, b//2, c) **2 %c
    else:
        return (dac(a, b//2, c)**2*a)%c
    
a, b, c = map(int, input().split())
print(dac(a, b, c))

'''
11:52~12:02 (10m) 시간 초과
    두배씩 계산하면서 시간 줄였다 생각했는데, 어떻게 고쳐야 될까?

10:34~40 (6m) 틀렸습니다
    숫자가 커지면 연산 시간이 길어져서, 연산 과정 중 % 구하기
    와 cnt가 b를 넘어가는 경우를 생각하지 못했다 조건이 cnt<b가 아니라 cnt*2<b 여야 함

~47 (7m) 시간 초과
a, b, c = map(int, input().split())
result = a*a
cnt = 2
while True:
    if cnt*2 < b:
        result = result * result %c
        cnt *= 2
    else:
        break
for _ in range(b-cnt):
    result = result * a %c
print(result)

    풀이 공부, 나중 다시 풀어보기 -> Solved in 11m
'''