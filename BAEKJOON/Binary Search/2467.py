# Solved (42m) w/ Search
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N-1
min_val = float('inf')
ans = []
while start < end: # 같은 수를 중복 탐색하면 안되므로 = 제거
    cur = arr[start] + arr[end]
    if abs(cur) < abs(min_val):
        min_val = cur
        ans = [arr[start], arr[end]]

    if cur < 0:
        start += 1
    else:
        end -= 1
print(*ans)
'''
2:32~42 (10m) 틀렸습니다
    조건이 1e9 이하니깐. 그떄도 ans를 가지려면 if abs(cur) < abs(min_val) 에 = 추가

47~00 (13m) python, pypy 시간 초과
    else 문 안에서 cur < 0인지 여부를 다시 검사하고 있어서, cur의 절댓값이 min_val 보다 큰 상태에서만 포인터 이동함
    else 블록 사용 X

~13 (13m) 숫자 올라가다가 틀렸습니다
    min_val 초기값을 1e9에서 float('inf')로 바꾸고, 
    min_val 업데이트 조건 abs(cur) <= abs(min_val) 에서 = 제거
    // 이전 코드는 왜 틀린걸까?
        모든 수가 1e9 근처로 주어져서 두 수를 합했을 때 min-val 보다 작아지는 경우가 없을 수도 있음. 그러면 ans에 아무 값도 안들어감
        두 값의 합을 보고 있기 때문에, abs(cur) < abs(min_val) 에 =를 추가한다고 값이 들어갈꺼라고 생각하면 안 됨

~20 (7m) Solved
'''