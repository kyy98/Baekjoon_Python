from collections import deque

def solution(prices):
    p_dq = deque(prices)
    ans = []
    while p_dq:
        v = p_dq.popleft()
        cnt = 0
        for n in p_dq:
            cnt+=1
            if v>n:
                break
        ans.append(cnt)
    return ans
    