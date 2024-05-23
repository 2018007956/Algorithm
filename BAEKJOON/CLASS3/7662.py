# Solved (22m) after Code Study
import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    check = [1] * (k)
    for i in range(k):
        x, n = input().split()
        if x=='I':
            n = int(n)
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
        else: # D
            if n=='-1' and min_heap:
                check[heapq.heappop(min_heap)[1]]=0
            elif n=='1' and max_heap:
                check[heapq.heappop(max_heap)[1]]=0

        # Synchronize
        while min_heap and check[min_heap[0][1]]==0:
            heapq.heappop(min_heap)
        while max_heap and check[max_heap[0][1]]==0:
            heapq.heappop(max_heap)
        
    if min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')

'''
deque는 pop(index) 형태 없음
Q = Q[:min_idx] + Q[min_idx+1:] 형태의 slicing도 TypeError: sequence index must be integer, not 'slice' 에러 발생
-> list로 수정

index로 찾아서 pop 방식으로 구현하면 시간 초과 날 것 같은데
시간 제한이 6초이고, T범위 안주어지고, k<=10^6.. 잘 모르겠음 -> 실제로 넣었더니 시간 초과

Q.pop(), Q=Q[1:] 로 수정 -> 1% 시간 초과
(주어진 문제 조건과 알고리즘을 따져서 시간 초과가 날 것이라는 객관적 도출이 어려움)

heapq 사용
Ref) https://codio.tistory.com/entry/%EB%B0%B1%EC%A4%80-7662%EB%B2%88-%EC%9D%B4%EC%A4%91-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC

point : check 배열 만들어서 두 배열 동기화, 원소들을 (숫자, index)로 저장하여 check 배열 접근
'''