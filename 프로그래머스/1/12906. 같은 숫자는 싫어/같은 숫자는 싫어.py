
def solution(arr):
    prev = -1
    ans = []
    for i in arr:
        if prev != i:
            ans.append(i)
            prev = i
    return ans
            
        
    # ans = [arr[0]]
    # for i in range(1, len(arr)):
    #     if ans[-1] != arr[i]:
    #         ans.append(arr[i])
    #     else:
    #         ans.pop()
    #         ans.append(arr[i])
    # return ans
        

            
        

        
        
        
    
    
        
                