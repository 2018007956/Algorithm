# Solved (1h 40m)
import sys
input = sys.stdin.readline

def floyd():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                time[i][j] = min(time[i][j], time[i][k] + time[k][j])
                if time[i][i] < 0: # 여기서 조건 검사하여 시간 단축
                    return "YES"
    return "NO"

for tc in range(int(input())):
    N, M, W = map(int, input().split())
    time = [[N*10000] * (N+1) for _ in range(N+1)]
    for _ in range(M): # road
        S, E, T = map(int, input().split())
        if T < time[S][E]: 
            time[S][E] = T
            time[E][S] = T
    for _ in range(W): # wormhole
        S, E, T = map(int, input().split())
        if -T < time[S][E]:
            time[S][E] = -T
    
    print(floyd())
'''
floyd warshall로 모든 지점부터 모든 지점까지의 최단 거리를 구했고, 여기서 time이 음수가 되는 경우가 있으면 YES인 것이라 생각했는데, 예시와 다름
    출발 위치에서 다시 돌아와야 함 (i->j) + (j->i)

~29 (42m) 시간 초과
    플로이드워셜은 시간복잡도가 O(n^3) = 500^3 = 1.2 *10^8
    다익스트라는 자료구조에 따라 O(n^2) 또는 O(nlogn)
    다익스트라를 n번 돌리면 O(n^3) 또는 O(n^2 logn)
PyPy3 로 제출해보니 73?74%에서 틀렸습니다
    입력 받을 때 최소값으로 받기 
    "웜홀 입력값 time[S][E]이 이미 road에서 입력받은 케이스 일 수 있음"을 간과
    
38~59 (21m) 91% 시간초과
    floyd 계산 하면서 동시에 음수 체크하고, 음수면 바로 동작 종료 및 YES 출력

~36 (37m) Solved w/ PyPy3
'''