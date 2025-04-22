citations = [3, 0, 6, 1, 5]

def solution(citations):
    cit = sorted(citations, reverse=True)
    for i in range(len(cit)):
        if cit[i] < i+1:
            return i
            
    return len(citations)
solution(citations)            
            


            
        
            
            
            
            
        