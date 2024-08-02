# 풀이 공부
import sys
input = sys.stdin.readline

N = int(input())

a,b,c = map(int, input().split())
max_ = [a,b,c]
min_ = [a,b,c]

for _ in range(N-1):
    one, two, three = map(int, input().split())

    max_0 = one + max(max_[0], max_[1])
    min_0 = one + min(min_[0], min_[1])

    max_1 = two + max(max_[0], max_[1], max_[2])
    min_1 = two + min(min_[0], min_[1], min_[2])

    max_2 = three + max(max_[1], max_[2])
    min_2 = three + min(min_[1], min_[2])

    max_ = [max_0, max_1, max_2]
    min_ = [min_0, min_1, min_2]

print(max(max_), min(min_))

'''
11:37~12:00 (23m) 메모리 초과
    길이 2짜리 배열 3개밖에 없는데 왜 메모리 초과?
    N이 매우 큰 값일 경우, board 배열을 한 번에 할당하는 것이 메모리 제한을 초과할 수 있다
    입력을 받는 동시에 값 계산하도록 구현해보기

~12:11 (11m) 3% 틀렸습니다
[내가 생각해낸 반례]
3
3 2 1
6 2 1
1 1 9
[정답]
14 3

max가 3+6+1이 아니라 3+2+9이다
그런데 현 코드에서 max가 3+6+1이 나올거라 생각했는데 17이 나왔다
위에서 뭘 선택해주냐에 따라 다음 열에서 고려될 값이 결정되는데, 이 부분을 구현해주지 않았다
값이 같은 경우에는 그 다음 열까지 고려해줘야 한다 -- 복잡

https://www.acmicpc.net/board/view/80155
    전 칸에서 왔을 수 있는 칸들 중 max min 값 더하는 방식으로 구현
    (두 코드의 차이)
        첫 번째 코드 : 현재 라인의 max, min 값 계산
        두 번쨰 코드 : 전 라인의 max, min 값 계산
    => 두 번째 코드로 Solve가 뜬 이유
        /// 좀 더 고민해보기

4:22~5:22 (1h) 풀이 공부
'''