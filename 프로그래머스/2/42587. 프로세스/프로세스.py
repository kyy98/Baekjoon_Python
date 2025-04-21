priorities = [2, 1, 3, 2]
location = 2

from collections import deque

def solution(priorities, location):
    cnt = 0
    q = deque([(v, i) for i, v in enumerate(priorities)])
    
    while q:
        current = q.popleft()
        if any(current[0] < i[0] for i in q):
            q.append(current)
        else:
            cnt+=1
            if current[1] == location:
                return cnt
solution(priorities, location)
    
    
    
    
    
    
    
    
    
    
    
    
#     cnt = 0
#     queue = deque([(v, i) for i, v in enumerate(priorities)])
    
#     while queue:
#         current = queue.popleft()
#         if any(current[0] < i[0] for i in queue):
#             queue.append(current)
#         else:
#             cnt+=1
#             if current[1] == location:
#                 return cnt
# solution(priorities, location)