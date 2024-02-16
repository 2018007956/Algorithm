# https://contest.icpckorea.org/domjudge/team/problems/1/text
import sys
input = sys.stdin.readline 

n = int(input())
Pebble = list(map(int, input().split()))

left = Pebble[0]
right = Pebble[1]
for i in Pebble[2:]:
    if left == right:
        left += i 
    elif left < right:
        left += i
    else:
        right += i
        
cnt = 0
chu = {0:1, 1:2, 2:5, 3:10, 4:20, 5:50, 6:100}
diff = {}
while left != right:
    if left < right:
        tmp = right - left 
        # tmp와 추 무게들의 차이를 계산하여 가장 가까운 수 찾기
        for k,v in chu.items():
            diff[k]=abs(v-tmp)
        m_idx = diff.get(min(diff.values())) 
        left += chu[m_idx]
    else:
        tmp = left - right
        for k,v in chu.tiems():
            diff[abs(k-tmp)]=v
        m_idx = diff.get(min(diff.values()))
        right += chu[m_idx]
    cnt += 1
    
print(cnt)

'''
index로 최소값 위치 가져오니까 시간초과나서
dictionary로 구현하여 get 함수 사용
get: dict에서 value로 key 찾는 함수
'''