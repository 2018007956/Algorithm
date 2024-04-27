# Solved (24m)
def fibonacci(n):
    cache = [(1,0), (0,1)]
    for i in range(2, n+1):
        cache.append((sum(cache[i-2]), sum(cache[i-1])))
    return cache[n]

T = int(input())
for _ in range(T):
    N = int(input())
    result = fibonacci(N)
    print(result[0], result[1])

'''
1초 -> 10^8
0.25초 -> 2.5*10^7, 0 <= N <= 40 

<피보나치 수열 구하는 알고리즘>
1. 재귀함수
시간복잡도 O(N^2) => 시간초과
2. DP
시간복잡도 O(N) => 성공
3. 행렬 멱법
점화식을 행렬화 시켜서 푸는 방법
시간복잡도 O(logN)
(참고 사이트 : https://myjamong.tistory.com/305)
'''