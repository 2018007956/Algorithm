# Solved (7m)
def solution(operations):
    queue = []
    for operation in operations:
        alpha, num = operation.split()
        if alpha == "I":
            queue.append(int(num))
        elif queue and alpha == "D":
            if num == "1": # 최댓값 삭제
                queue.pop(queue.index(max(queue)))                
            elif num == "-1": # 최솟값 삭제
                queue.pop(queue.index(min(queue)))
    if queue:
        return [max(queue), min(queue)]
    else:
        return [0,0]


# 다른 사람 풀이
import heapq
def solution(operations):
    heap = []
    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)
        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
                # 특정 항목을 찾아서 삭제했을 경우, 다시 이진트리 형태로 만들어줘야 함
                # (특정 항목을 삭제하고자 할 경우, 삭제하는 정보를 담은 별도의 자료형을 만들거나, 힙 자료형에 삭제/보전 하는 정보를 담은 형태로 값을 저장하는게 좋음)
                heapq.heapify(heap)

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]