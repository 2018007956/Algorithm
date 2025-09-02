import math
def solution(n, w, num):
    
    top_level = math.ceil(n/w) # 4
    num_level = math.ceil(num/w) # 2
    
    top_level_blockNum = n - w * (top_level-1) # 4
    cur_level_blockNum = num - w * (num_level-1) # 2
    # 같은 방향인 경우
    if (top_level%2==1 and num_level%2==1) or (top_level%2==0 and num_level%2==0):    
        if top_level_blockNum >= cur_level_blockNum:
            answer = top_level - num_level + 1
        else:
            answer = top_level - num_level
    # 다른 방향인 경우
    else:
        if top_level_blockNum + cur_level_blockNum > w:
            answer = top_level - num_level + 1
        else:
            answer = top_level - num_level        
    
    return answer


''' 다른 사람 풀이 '''
def solution(n, w, num):
    m1 = num%(w*2)
    m2 = ((w*2+1) - m1)%(w*2)
    # num 이상 n 이하의 수들 중 2*w로 나눈 나머지가 m1,m2인 것들의 수를 세면 된다.
    return len(range(num,n+1,w*2)) + len(range(num + (m2-m1)%(w*2), n+1, w*2))


def solution(n, w, num):
    top = (n-1)//w+1
    row = (num-1)//w+1
    col = (num-1)%w
    top_col = (n-1)%w
    if top%2==row%2:
        return top-row + (0 if top_col<col else 1)
    else:
        return top-row + (0 if top_col+col<w-1 else 1)