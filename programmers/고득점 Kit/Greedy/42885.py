# Not Solved
def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boats = 0

    while left<=right:
        if people[left]+people[right]<=limit:
            left+=1
        right-=1
        boats+=1
        
    return boats
'''
정렬해서, 작은 숫자부터 뒤의 큰 숫자들과 비교!

두 명까지 태울 수 있고, 합이 limit 이하인 경우에만 짝이 가능하다
👉 정렬된 배열의 양 끝에서 가장 효율적인 짝을 찾는 투포인터 구조

[투포인터 + 그리디]
1. 정렬
제한된 자원에서 최대한 효율적으로 짝을 지어야 하는 문제는 대부분 정렬이 먼저 떠오름
정렬하면 가장 가벼운 사람과 가장 무거운 사람이 누군지 쉽게 알 수 있음

2. 무거운 사람을 먼저 처리해야 함
무거운 사람은 혼자 탈 수도 있음
가능한 한 가벼운 사람과 짝지을 수 있으면 가장 이상적

3. 가벼운 사람과 짝지을 수 있을까?
이 판단을 위해선 양쪽 끝에서 확인하는 게 좋음:
    가장 가벼운 사람 people[left]
    가장 무거운 사람 people[right]
둘이 limit 이하이면 같이 태움, 아니라면 무거운 사람만 태움

=> 투포인터 구조 사용
'''