import queue
N = int(input())
q = queue.Queue()
for i in range(1, N+1):
    q.put(i)
while q.qsize()!=1:
    q.get()
    q.put(q.get())
print(q.queue[0])

'''
list로 아주 단순하게 짰는데 시간초과
    lst.pop(0)
    lst.append(lst.pop(0))

'''