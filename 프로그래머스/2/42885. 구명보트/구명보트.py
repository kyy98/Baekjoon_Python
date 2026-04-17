# 투포인터
def solution(people, limit):
    people.sort()
    start = 0
    end = len(people)-1
    
    cnt = 0
    while start<end:
        sum = people[start]+people[end]
        if sum <= limit:
            cnt+=1
            start+=1
        end-=1
    
    return cnt+(len(people)-2*cnt)
        