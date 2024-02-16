import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
while start <= end:
    mid = (start + end) // 2
    get = sum(i - mid if i - mid > 0 else 0 for i in tree) 
    if get < M:
        end = mid - 1
    else:
        start = mid + 1
print(end)



'''
나무 최대 길이부터 M값이 될 때까지 1씩 빼면서 나무 모음
cut = max(tree) - (M//len(tree)+1)
get = 0
while get < M:
    get = sum([x-cut for x in tree if x-cut > 0])
    cut -= 1
print(cut+1) # 마지막 조건 맞춰졌을때 밑줄에서 -1되므로 결과값 +1 해줌

**시간초과**
N이 백만이기 때문에 N크기의 리스트를 돌며 확인하는 것은 시간복잡도가 n^2
-> 이분 탐색으로 mid 값을 잡으면서 계산
'''