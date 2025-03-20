# 풀이 공부
def solution(n, times):
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left+right)//2
        people = 0 # 심사한 사람 수

        for time in times:
            people += mid//time
            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

'''
1. input의 최대길이가 지나치게 길고, 특정 값을 찾아야 하는 문제라면 이분탐색을 의심해보자
2. 이분탐색의 전반적인 구조를 외우도록 하자 (left, right, while, for, break, if...)
'''