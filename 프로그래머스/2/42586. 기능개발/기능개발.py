from collections import deque
import math
def solution(progresses, speeds):
    num = deque([])
    ans = []
    for i in range(len(progresses)):
        num.append(math.ceil((100-progresses[i])/speeds[i]))
    
    while num:
        cnt = 1
        v = num.popleft()
        while num:
            c = num.popleft()
            if v>=c:
                cnt+=1
            else:
                num.appendleft(c)
                break
        ans.append(cnt)
    return ans