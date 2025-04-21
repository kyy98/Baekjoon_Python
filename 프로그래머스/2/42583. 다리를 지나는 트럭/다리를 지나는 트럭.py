bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# def solution(bridge_length, weight, truck_weights):
#     cnt = 1
#     for i in range(len(truck_weights)-2):
#         if truck_weights[i]+truck_weights[i+1] > 10:
#             cnt+=2
#         else:
#             cnt+=4
#     cnt+=1
#     return cnt
# solution(bridge_length, weight, truck_weights)

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  
    truck_weights = deque(truck_weights) 
    current_weight = 0
    
    while truck_weights:
        current_weight -= bridge.popleft()
        
        if current_weight + truck_weights[0] <= weight:
            current_weight+=truck_weights[0]
            bridge.append(truck_weights.popleft())
            time+=1
          
        else:
            bridge.append(0)
            time+=1
    return time+bridge_length
solution(bridge_length, weight, truck_weights)

        
    
    
    
    
    
    
    
    
#     while len(truck_weights) > 0:
#         time += 1
#         currentWeight -= bridge.popleft()
        
#         if currentWeight+truck_weights[0] <= weight:
#             currentWeight += truck_weights[0]
#             bridge.append(truck_weights.popleft())
#         else:
#             bridge.append(0)
#     time+=bridge_length
#     return time
# solution(bridge_length, weight, truck_weights)
            
            
        
            
        
    
    