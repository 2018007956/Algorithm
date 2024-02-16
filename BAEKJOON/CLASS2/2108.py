import sys
from collections import Counter
N = int(sys.stdin.readline()) #int(input())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

print(int(round(sum(arr)/N)))
print(arr[N//2])
cnt = Counter(arr).most_common()
mode = []
for i in cnt:
    if i[1]==cnt[0][1]:
        mode.append(i[0])
print(sorted(mode)[1] if len(mode)>1 else mode[0])
print(max(arr)-min(arr))