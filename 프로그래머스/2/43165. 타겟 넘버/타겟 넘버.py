from collections import deque

def solution(numbers, target):
    q = deque([(0,0)])
    answer = 0
    
    while q:
        idx, res = q.popleft()
        if idx == len(numbers):
            if res == target:
                answer+=1
        else:
            q.append((idx+1, res+numbers[idx]))
            q.append((idx+1,res-numbers[idx]))
    return answer