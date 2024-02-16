#26110
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

result = []
def palindrome(st):
    global cnt 
    if cnt >=4:
        print(st, cnt)
        result.append(-1)
        return
    if len(st)==0 or len(st)==1:
        print(st, cnt)
        result.append(cnt)
        return

    print('---',st[0],st[-1],st[0]==st[-1])
    if st[0]==st[-1]:
        print('same',st,cnt)
        palindrome(st[1:-1]) 
    else:
        cnt += 1
        print(st, cnt)
        # rm left
        palindrome(st[1:])
        # rm right
        palindrome(st[:-1])
        
    

cnt = 0
s = input().strip()
palindrome(s)
print(result)
print(min(result))

'''
조건에 맞지 않는 재귀함수에 들어가는 이유가 뭘까?

'''