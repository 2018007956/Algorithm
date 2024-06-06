# Solved (7m)
next_num = 0
for i in range(3,0,-1):
    num = input()
    if num.isdigit():
        next_num = int(num) + i

if next_num %3==0:
    print('Fizz', end='')
if next_num %5==0:
    print('Buzz', end='')
if next_num %3!=0 and next_num %5!=0:
    print(next_num)
    
'''
3개 모두 문자열인 경우는 없음
숫자를 찾아서 다음 올 수를 예측
'''