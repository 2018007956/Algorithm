# 풀이 공부 (1h 40m)
number = str(input())
result = 1
idx = 0
while idx < len(number):
    for ch in str(result):
        if idx < len(number) and ch == number[idx]:
            idx += 1
    result += 1
print(result-1)
'''
예외케이스 : 111111 -> 14
for char in str(input())으로 확인하면 한글자씩 밖에 확인 못하기 때문에
인덱스로 접근해야 함
'''