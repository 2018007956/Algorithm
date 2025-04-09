# Solved
def solution(citations):
    citations.sort()
    left, right = 0, len(citations)
    while left <= right:
        mid = (left+right)//2
        cnt = sum(1 for x in citations if x >= mid)        
        if cnt >= mid:
            h = mid
            left = mid + 1
        else:
            right = mid - 1
    return h

## 최적화 O(N logN)->O(N)
# 인용 횟수를 내림차순으로 정렬하고, 인덱스 자체를 활용하면 이진탐색 없이도 풀이 가능
def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for i, citation in enumerate(citations):
        if citation >= i+1:
            h = i+1
        else:
            break
    return h
'''
Idea> 현재까지 살펴본 논문의 개수(i+1)가, 그 논문들의 인용 횟수(citation) 이상이다.
    즉, 현재까지 살펴본 논문이 모두 H-index 조건을 만족하는 상태
'''
def solution(citations):
    citations.sort(reverse=True)
    return max(min(i+1, c) for i, c in enumerate(citations))

# start=1 : index를 1부터 시작
def solution(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))