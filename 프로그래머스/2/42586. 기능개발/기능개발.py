# import math
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

# def solution(progresses, speeds):
#     ls = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    
#     answer = []
#     idx = 0
#     for i in range(len(ls)):
#         if ls[idx] < ls[i]:
#             answer.append(i-idx)
#             idx = i
#     answer.append(len(ls)-sum(answer))
#     return answer

# solution(progresses, speeds)
            
        
progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0
    while len(progresses)>0:
        if progresses[0] + time*speeds[0] >= 100:
            cnt+=1
            progresses.pop(0)
            speeds.pop(0)  
            
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
                time+=1
            else:
                time+=1
    answer.append(cnt)
    return answer
solution(progresses, speeds)
            
            

        