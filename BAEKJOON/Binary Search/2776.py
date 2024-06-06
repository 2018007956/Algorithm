# Solved (6m)
# Sol1) Hash map
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr1 = {}
    for x in map(int, input().split()):
        arr1[x] = 1
    M = int(input())
    for y in map(int, input().split()):
        try:
            print(arr1[y])
        except:
            print(0)

# Sol2) Binary Search
def binary_search(x):
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == x:
            return 1
        elif arr1[mid] > x:
            end = mid -1
        else:
            start = mid + 1
    return 0

for _ in range(T):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr1.sort()
    M = int(input())
    for y in map(int, input().split()):
        print(binary_search(y))