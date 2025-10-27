from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    bridge_weight = 0
    while truck_weights:
        answer += 1

        bridge_weight -= bridge.popleft()
        
        if bridge_weight + truck_weights[0] <= weight:
            bridge_weight += truck_weights[0]
            truck = truck_weights.popleft()
            bridge.append(truck)
        else: 
            bridge.append(0)
    answer += bridge_length
        
    return answer