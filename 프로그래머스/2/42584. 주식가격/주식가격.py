from collections import deque
def solution(prices):
    answer = []
    prices_dq = deque(prices)
    while prices_dq:
        k = prices_dq.popleft()
        cnt=0
        for p in prices_dq:
            if k > prices_dq[0]:
                cnt+=1
                break
            else:
                cnt+=1
                if k > p:
                    break
        answer.append(cnt)
                
    return answer