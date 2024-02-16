import math
A, B, V = map(int, input().split())
print(math.ceil((V-A)/(A-B))+1)

'''
while문으로 하나씩 더하고 빼면서 날짜 count하면
input으로 1000000000이 들어왔을때 처리가 너무 오래걸림

바로 연산하는 식으로 가야될 것 같은데,
(A-B)*며칠+A>=V
-> (V-A)/(A-B) 의 올림
-> 근데 왜 +1을 해야 맞는 값이 나오는지 모르겠음

다른 사람 코드를 보니
A * day - B * (day-1) >= V
day >= (V+B)/(A/B)
math.ceil((V-B)/(A-B))

내 코드는
A * (day+1) - B * day >= V
이기 때문에 day가 0부터 가능하므로 
마지막에 +1 해줘야 함
'''