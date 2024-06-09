# Solved (33m) w/ Search
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(M):
    x1,y1, x2,y2 = map(int, input().split())

    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]    
    print(result)
    
'''
8:52~12 (20m) 1% 시간 초과
    sum(sum([row[y1-1:y2] for row in arr[x1-1:x2]],[]))
    sum([sum(row[y1-1:y2]) for row in arr[x1-1:x2]])
    sum은 O(n)의 시간복잡도를 가짐
    입력 받을 때 누적합으로 받아서 마이너스 계산만 해보자
~47 (35m) 시간 초과
    arr 생성 X 바로 cumulate 만들기
    M * (x2-(x1-1)) = 100,000 * 100,000 이므로 for i in range(x1-1, x2)를 쓰면 안될 것 같다
    1차원 리스트로 누적합을 구해볼까?

(시간 초과 발생 코드)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cumulate = [[0]*(N) for _ in range(N)]
for i in range(N):
    for j in range(N):
        cumulate[i][j] = cumulate[i][j-1]+arr[i][j]
print(cumulate)
for _ in range(M):
    x1,y1, x2,y2 = map(int, input().split())
    result = 0
    for i in range(x1-1,x2):
        if y1-2==-1: # 첫번째열인 경우
            result += cumulate[i][y2-1]
        else:
            result += cumulate[i][y2-1]-cumulate[i][y1-2]
    print(result)

~54, 10:04~20 (23m) 풀이 확인
    Ref) https://codingwonny.tistory.com/306
    사각형 모양 통으로 교집합 합집합 생각해야 됨. 

다음에 다시 풀어보기 -> Solved in 33m 
'''