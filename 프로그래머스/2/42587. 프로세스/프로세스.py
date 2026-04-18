from collections import deque
def solution(priorities, location):
    answer = []
    num = deque([(i, p) for i, p in enumerate(priorities)])
    
    while num:
        v = num.popleft()
        if any(v[1]<q[1] for q in num):
            num.append(v)
        else:
            answer.append(v)
    for a in answer:
        if a[0] == location:
            ans = answer.index(a)+1
    return ans