# Not Solved
from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    weighted_truck = deque(truck_weights)
    cur_bridge = deque([0] * bridge_length) # 다리의 길이만큼 0으로 초기화 (각 자리에 트럭의 무게를 기록)
    cur_weight = 0
    
    while weighted_truck or cur_weight > 0:
        # 다리 위 트럭들의 이동
        cur_weight -= cur_bridge.popleft()
        
        # 새로운 트럭이 올라갈 수 있으면 올린다
        if weighted_truck and cur_weight + weighted_truck[0] <= weight:
            truck = weighted_truck.popleft()
            cur_bridge.append(truck)
            cur_weight += truck
        else:
            cur_bridge.append(0)
        
        time += 1
    return time