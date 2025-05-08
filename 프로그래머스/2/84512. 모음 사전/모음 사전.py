from itertools import product

# def solution(word):
#     result = []
#     for i in range(1, 6):
#         ls = list(product(["A", "E", "I", "O", "U"], repeat=i))
#         for j in ls:
#             result.append(''.join(j))
#     result = sorted(result)
#     return result.index(word)+1
            
            
def solution(word):
    ls = []
    for i in range(1,6):
        m = ['A', 'E', 'I', 'O', 'U']
        p = list(product(m, repeat = i))
        for i in p:
            ls.append(i)
    num = [''.join(j) for j in ls]
    return sorted(num).index(word)+1
        

        
    
        
    
        
        
        
        
        
        
        
        
        
## itertools.product(1~5)
## 그리고 sort
## idx+1