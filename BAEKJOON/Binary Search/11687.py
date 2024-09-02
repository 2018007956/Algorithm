# 풀이 공부
def find_right_zeros(n):
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
    return zeros
    ## 아래 코드는 시간초과 발생 
    # cnt = 0
    # for x in reversed(str(math.factorial(n))):
    #     if x=='0':
    #         cnt += 1
    #     else:
    #         break
    # return cnt

M = int(input())
res = -1
start, end = 5, M * 5
while start <= end:
    mid = (start + end) // 2

    if find_right_zeros(mid) >= M:
        res = mid
        end = mid -1
    else:
        start = mid + 1

print(res if find_right_zeros(res)==M else -1)
'''
end를 임의로 50정도로 잡으면 예제는 다 잘 돌아가는데, end 초기값을 뭘로 지정해줘야 할지 모르겠음

마지막 0의 개수가 최대 100,000,000개가 되려면
len(str(math.factorial(1000))) = 2568 이고, len(str(math.factorial(10000)))은 exceeds the limit 나는데, 
end를 어떻게 잡아야 하지?

(답안 참고)
정수론 원리 이용 : N!의 오른쪽 0의 개수 = N을 5로 나누면서 생기는 몫들의 합
    0이 생기는 이유는 10 = 2*5 이기 때문에, 팩토리얼 계산 중 5가 얼마나 많이 곱해지는지를 세는 것이다.

위 개념을 알고보니까 예제 출력값이 모두 5의 배수였다. 
**주어진 범위를 생각해봐도 end를 어떻게 정의해야 할 지 모르겠을땐 주어진 변수와 연관지어서 생각해보기**

(이 문제는 이분탐색 활용보다 0의 개수를 어떻게 효율적으로 찾을 것인지가 핵심인 문제)
'''