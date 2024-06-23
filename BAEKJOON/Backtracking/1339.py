# Solved (1h 7m)
N = int(input())
words = [input() for _ in range(N)]

data = {}
for x in words:
    tmp = 1
    for i in x[::-1]:
        if i not in data:
            data[i] = tmp
        else:
            data[i] += tmp
        tmp *= 10  # 이미 넘버링 된 알파벳도 자릿수는 고려해줘야 하기 때문에 if문 바깥에서 매 루프마다 1씩 증가함
# print(data)

re_numbering = 9
for k, v in sorted(data.items(), key=lambda x:x[1], reverse=True):
    data[k] = re_numbering
    re_numbering -= 1
# print(data)

result = []
for x in words:
    num = ''
    for i in x:
        num += str(data[i])
    result.append(int(num))
print(sum(result))


'''
GCF + ACDEB
321   54321
숫자 큰 순서대로 9부터 할당

set을 사용하면 순서가 없어짐 -> Collection Package의 OrderedDict 사용하면 순서 유지하면서 중복 제거 가능

9:31~35, 38~10:15 (41m) 틀렸습니다
반례) 10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB
output: 1780(A=9, B=8)
answer: 1790(A=8, B=9)

단순히 자릿수만 고려해주면 안된다. 숫자 개수도 중요하네
=> 내가 푼 풀이로는 안될듯. 알고리즘 갈아엎어야 됨
(내가 푼 풀이)
from collections import OrderedDict
N = int(input())
words = [input() for _ in range(N)]

data = {}
for x in set(words):
    tmp = 1
    for i in list(OrderedDict.fromkeys(x))[::-1]:
        if i not in data:
            data[i] = tmp
        tmp += 1  # 이미 넘버링 된 알파벳도 자릿수는 고려해줘야 하기 때문에 if문 바깥에서 매 루프마다 1씩 증가함
# print(data)

re_numbering = 9
for k, v in sorted(data.items(), key=lambda x:x[1], reverse=True):
    data[k] = re_numbering
    re_numbering -= 1
# print(data)

result = []
for x in words:
    num = ''
    for i in x:
        num += str(data[i])
    result.append(int(num))
print(sum(result))


자릿수를 셀때 10의 단위로 세서 개수까지 고려해주기 / 중복제거 하면 안됨, Solved in 26m
'''