T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    queue = [i for i in enumerate(lst)]

    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == M:
                print(answer)
                break