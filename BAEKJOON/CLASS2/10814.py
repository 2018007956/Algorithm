N = int(input())

arr = []
for i in range(N):
    age, name = input().split()
    arr.append([int(age), name])

arr.sort(key=lambda x:x[0])
for i in arr:
    print(i[0], i[1])

'''
틀린 이유: age가 문자열로 들어가서
나이 100과 20을 비교할때 100<20 이 됨 - 뭔진 모르겠지만 비교가 제대로 안됨

그래도 틀린 이유: 이름이 같은 경우가 있음
list 이용

또 틀림: arr.sort()로만 하면 0,1 인덱스 모두 정렬됨
20 B
20 A
-> 20 A
   20 B
   로 출력됨
arr.sort(key=lambda x:x[0])
'''