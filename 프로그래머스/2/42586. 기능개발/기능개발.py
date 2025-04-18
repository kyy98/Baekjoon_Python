import math
progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    ls = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    
    answer = []
    idx = 0
    for i in range(len(ls)):
        if ls[idx] < ls[i]:
            answer.append(i-idx)
            idx = i
    answer.append(len(ls)-sum(answer))
    return answer

solution(progresses, speeds)
            
        
            
            

        