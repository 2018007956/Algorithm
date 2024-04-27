# Solved (22m)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
cumulate = [0]
for idx, num in enumerate(arr):
    cumulate.append(cumulate[idx]+num)

for _ in range(M):
    i, j = map(int, input().split())
    print(cumulate[j]-cumulate[i-1])

'''
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N

slicing하여 sum 함수로 푸는 방식 (구간합)은
시간복잡도가 O(n)이며 m번동안 수행하게 되면 O(nm)이므로 시간초과 발생
=> 매번 구간합을 구하는 것이 아닌, 처음에 입력받을 때 누적합을 계산하여 저장

input() 했을 때 시간초과 발생
=> sys.stdin.readline()으로 수정하여 Solved
'''