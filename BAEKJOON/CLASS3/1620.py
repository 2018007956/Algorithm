# Solved (15m)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

call_num, call_name = {}, {}
for cnt in range(1,N+1):
    name = input().strip()
    call_num[cnt] = name
    call_name[name] = cnt

result = []
for _ in range(M):
    tmp = input().strip()
    if tmp.isdigit():
        result.append(call_num.get(int(tmp)))
    else:
        result.append(call_name.get(tmp))
        
for i in result:
    print(i)


'''
12:11~12:23 (12m) 시간초과
1 ≤ N ≤ 100,000, 1 ≤ M ≤ 100,000
[k for k,v in dogam.items() if v==tmp][0] -> 시간복잡도 O(n)
-> 최악의 경우 O(nm) = 10,000,000,000 (100억번)

12:28~12:31 (3m) Solved
value를 가지고 key를 뱉는 형태를
저장할 때 dict을 두 개로 저장해서 즉시 호출 가능하도록 수정
'''