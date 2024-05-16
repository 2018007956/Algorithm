# Solved (19m)
import sys
sys.stdin = open("input.txt", "r")

for t in range(1,11):
    N = int(input())
    height = list(map(int, input().split()))

    answer = 0
    for i in range(2,N-1):
        if height[i]==max(height[i-2:i+3]):
            answer += height[i]-max(height[i-2:i]+height[i+1:i+3])
    print(f'#{t} {answer}')