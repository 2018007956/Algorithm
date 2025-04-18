# Not Solved - Too hard
def solution(name):
    answer = 0
    n = len(name)
    
    # 1. 상하 조작 횟수
    for char in name:
        up_down = min(ord(char)-ord('A'), ord('Z')-ord(char)+1)
        answer += up_down
        
    # 2. 좌우 조작 횟수 최적화
    move = n - 1 # 일단 오른쪽으로만 쭉 가는 경우로 초기화
    
    for i in range(n):
        next_idx = i + 1
        # 연속된 'A'가 끝나는 지점 찾기
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        distance = min(
            i*2+n-next_idx, # 오른쪽으로 i까지 갔다가 다시 왼쪽으로 돌아가서 끝까지 가는 경우 
            (n-next_idx)*2+i # 왼쪽으로 갔다가 오른쪽으로 돌아오는 경우
        )
        move = min(move, distance)
        
    answer += move
    return answer