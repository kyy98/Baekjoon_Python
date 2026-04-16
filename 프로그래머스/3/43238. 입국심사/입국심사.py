def solution(n, times):
    start = 1
    end = max(times)*n
    answer = end
    
    while start <= end:
        mid = (start+end)//2
        total = 0
        for t in times:
            total+=mid//t
        if total >= n:
            answer = mid
            end = mid-1
        else:
            start = mid+1
        
    
    return answer