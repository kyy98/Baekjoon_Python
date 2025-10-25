from collections import deque
def solution(priorities, location):
    answer = [] # 실행된 프로세스
    dq = deque((i, j) for i, j in enumerate(priorities))
    while dq:
        process = dq.popleft()
        if any(process[1] < q[1] for q in dq):
            dq.append(process)
        else:
            answer.append(process)
    for d in answer:
        if d[0] == location:
            return answer.index(d)+1
            
            
        
        