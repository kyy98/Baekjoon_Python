def solution(elements):
    ans = set()
    e_2 = elements*2
    
    for i in range(len(elements)):
        for j in range(len(elements)):
            ans.add(sum(e_2[i:i+j+1]))
            
    
    return len(list(ans))