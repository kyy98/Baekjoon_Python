from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    dq = deque([])
    
    for i in range(len(progresses)):
        day = math.ceil((100-progresses[i])/speeds[i])
        dq.append(day)
        
    while dq:
        cnt = 1
        d1 = dq.popleft()
        while dq:
            d2 = dq.popleft()
            if d1>=d2:
                cnt+=1
            else:
                dq.appendleft(d2)
                break
                
        answer.append(cnt)
    return answer