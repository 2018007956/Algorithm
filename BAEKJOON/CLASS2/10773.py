import sys
input = sys.stdin.readline

K = int(input())
arr = []
for i in range(K):
    x = int(input())
    if x == 0:
        arr.pop()
    else:
        arr.append(x)
print(sum(arr))

'''
처음엔 리스트로 안받고 sum으로 바로바로 더했는데 
이러면 0이 두번 연속 들어왔을 때 전전값을 뺄 수가 없음
-> 리스트로 구현
'''