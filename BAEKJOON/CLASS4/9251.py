# Solved (1h 7m) w/ Study
a = input()
b = input()
LCS = [[0] * (len(b)+1) for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])

'''
1:30~1:57 (27m) 1% 틀렸습니다
반례) 
ABAABA
AA
[정답] 2
[출력] 4
while문 안에서 바로 -1을 해주기 때문에(0을 고려하기 위함) len(vistedA)와 같은 경우도 조건으로 넣어줘야 마지막 값 방문체크함
(내 코드)
a = input()
b = input()
visitedA = [0] * len(a)
visitedB = [0] * len(b)
cnt = 0
for i, x in enumerate(a):
    for j, y in enumerate(b):
        if x==y and not visitedA[i] and not visitedB[j]:
            cnt += 1
            print(x)
            tmpi = i+1
            while 0<tmpi<=len(visitedA) and not visitedA[tmpi-1]:
                tmpi -= 1
                visitedA[tmpi] = 1
            tmpj = j+1
            while 0<tmpj<=len(visitedB) and not visitedB[tmpj-1]:
                tmpj -= 1
                visitedB[tmpj] = 1
            print('a',visitedA)
            print('b',visitedB)
            break
print(cnt)
~04 (7m) 틀렸습니다
반례)
qsdferrfgtfsawfsefeesgdtdrgthyytfgfddsdawdwd
efvs
[정답] 3
[출력] 1
문자열 a에서 먼저 탐색하고 있기 때문에 s를 탐색할 떄 visitedB가 모두 1로 바뀌게 됨
알고리즘을 뜯어고쳐야 할 것 같다. 답지보고 공부해보기 2:10~40 (30m)
Ref) https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence#longest-common-subsequence-substring
'''