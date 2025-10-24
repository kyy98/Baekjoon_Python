
def solution(arr):
    ls = [arr[0]]
    for i in range(1, len(arr)):
        if ls[-1] == arr[i]:
            ls.pop()
            ls.append(arr[i])
        else:
            ls.append(arr[i])
    return ls
   


        
        
        
    
    
        
                