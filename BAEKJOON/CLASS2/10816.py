import sys
from collections import Counter
_ = sys.stdin.readline()
N = sys.stdin.readline().split()
_ = sys.stdin.readline()
M = sys.stdin.readline().split()
C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))

'''
for i in M_lst:
    print(N_lst.count(i),end=' ')
-> 시간초과

count의 시간 복잡도는 O(N)
여기서 각각의 리스트의 개수를 확인하기 위해서는 for문을 통해 count를 n번하기 때문에 시간복잡도는 O(N2)

Counter 클래스를 이용해 Counter를 n번 하면 시간 복잡도는 O(N)
딕셔너리에서 원소를 접근할 때의 시간 복잡도는 O(1)이기 때문

count를 여러번 사용하는 경우는 Counter 클래스가 더욱 유용

그리고 어차피 출력시 string으로 바뀌니까 (f'{}')
입력 받을 때 map으로 int형으로 바꿔 받을 필요 없음
-> 여기서도 시간 초과 떠서 list(map(int, -)) 없앴더니 성공
'''