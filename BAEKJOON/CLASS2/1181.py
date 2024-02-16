N = int(input())
lst = {}
for i in range(N):
    a = input()
    lst[a] = len(a)
# Sort by Key
lst = {x:y for x,y in sorted(lst.items())}
# Sort by Value
lst = sorted(lst.items(), key=lambda item: item[1])
for i in lst:
    print(i[0])

'''
list.sort()
list.sort(key = len)
'''