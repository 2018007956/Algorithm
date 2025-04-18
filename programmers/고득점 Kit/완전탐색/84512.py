# Not Sovled
cnt = 0
ret = 0
visited = {}
def dfs(s):
    global cnt, ret, text
    if s == text:
        ret = cnt
        return

    if len(s) == 5:
        return

    elif ret == 0:
        for i in ["A", "E", "I", "O", "U"]:
            if s+i not in visited:
                visited[s+i] = 1
                cnt += 1
                dfs(s + i)


def solution(word):
    global text
    text = word
    dfs("")
    return ret

'''
"A", "AA", "AAA", "AAAA", "AAAAA", "AAAAE", "AAAAI", "AAAAO", "AAAAU", "AAAE"
이런 순서로 카운팅 되는 것을 보고, 백트래킹을 생각해낼 수 있어야 함
'''