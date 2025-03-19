# Solved (17m)
def check_one_diff(a, b):
    cnt = 0
    for x, y in zip(a, b):
        if x!=y:
            cnt += 1
            
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    result_cnt = 1e8
    visited = [False] * len(words)
    def dfs(cnt, word):
        nonlocal result_cnt
        if word == target:
            result_cnt = min(result_cnt, cnt)
        
        for idx, x in enumerate(words):
            if check_one_diff(word, x) and not visited[idx]:
                visited[idx] = True
                dfs(cnt+1, x)
                visited[idx] = False

    dfs(0, begin)
    return result_cnt

'''
하나만 다른지 찾는 방법? -> 함수 만듦
'''

# 다른 사람 풀이) Generator
from collections import deque

# 한 글자만 변경하여 만들 수 있는 단어들을 찾는 제너레이터 함수
def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}   # 각 단어까지의 변환 횟수를 저장
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)  # target 단어가 발견되면 변환 횟수를 반환하고, 불가능한 경우 0을 반환

'''
방문 여부를 사전형에 추가 되었는지 아닌지로 알 수 있다
'''