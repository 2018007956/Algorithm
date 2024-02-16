import collections
counter = collections.Counter(input().upper())

lst = list(counter.values())
max_idx = list(filter(lambda x: list(counter.values())[x]==max(lst), range(len(lst))))
# list(filter())를 이용해서 list안에 중복되는 value값이 있어도 다중의 index번호를 list로 줌

if len(max_idx)>1:
    print('?')
else:
    print(list(counter.keys())[max_idx[0]])