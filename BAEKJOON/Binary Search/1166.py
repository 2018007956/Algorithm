# Solved (1h 2m)
N, L, W, H = map(int, input().split())

start, end = 0, min(L, W, H)
for _ in range(100): # 100번 정도 돌리면 결과의 오차가 10**-9보다 작게 나온다고 함
    mid = (start + end) / 2

    # 상자들이 더 들어갈 수 있으면, 길이 mid 늘이기
    if (L//mid) * (W//mid) * (H//mid) >= N:
        start = mid
    else:
        end = mid

print(start)
'''
~00 (40m) 풀이 참고
소수점을 어떻게 처리해줘야할지 모르겠음
    조건이 만족할 때까지 탐색하는게 아니라 특정 횟수만큼 반복 후 종료
    start, end 값을 mid 값으로 업데이트
    반복문이 끝나면 start, end 둘 중 아무거나 출력

~7:15 (15m) 68%쯤 틀렸습니다
    mid는 정육면체 한 변의 길이 A를 뜻함
    A가 L, W, H 중 최소값보다 클 수가 있나?  없는데. 왜 max(L, W, H)이지?
    다른 풀이들은 end를 L, W, H의 max 값으로 지정해놨길래 위와 같은 고민을 했는데, 
    min은 맞았고(max 해도 답이 틀리진 않음 탐색 범위가 넓어질 뿐), start값이 틀린거였다. start = 1이 아니라 0
    참고) https://www.acmicpc.net/board/view/138860
    N, L, W, H 이 모두 1보다 크거나 같다고 해서 내가 정의내린 mid 도 자연스레 최소값이 1인줄 착각함
    **주어진 변수와 내가 정의한 mid 변수는 범위가 다를 수 있음을 간과**
    0 < mid <= min(L, W, H)

~22 (7m) Solved
'''