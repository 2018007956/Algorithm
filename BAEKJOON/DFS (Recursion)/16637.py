# 풀이 공부
def dfs(i, val):
    global max_val
    if i == N:
        max_val = max(max_val, int(val))
        return
    
    # 괄호 사용 O
    if i+4 <= N:
        dfs(i+4, str(eval(val+words[i] + str(eval(words[i+1:i+4])))))
    # 괄호 사용 X
    if i+2 <= N:
        dfs(i+2, str(eval(val+words[i:i+2])))


N = int(input())
words = input().rstrip()

max_val = float('-inf')
dfs(1, words[0])
print(max_val)
'''
10:30~50, 57~20 (43m) 괄호 넣는 부분 구현 아이디어 부족
처음에 짠 코드
def calculate(arr):
    # 앞에서 부터 계산
    res = int(arr[0])
    for i, x in enumerate(arr):
        if not x.isdigit():
            if x=='+':
                res += int(arr[i+1])
            elif x=='-':
                res -= int(arr[i+1])
            elif x=='*':
                res *= int(arr[i+1])
    return str(res)

# 괄호 넣기
arr2 = ''
for i in range(N):
    for j in range(i+1, N):
        if arr[i].isdigit() and arr[j].isdigit():
            arr2 = arr[:i] + '(' + arr[i:j+1] + ')' + arr[j+1:]
            print(arr2)
            print(calculate(arr[:i]+calculate(arr[i:j+1])+arr[j+1:]))


풀이 공부 Ref: https://jaehwaseo.tistory.com/20
'''