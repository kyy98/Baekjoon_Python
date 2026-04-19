def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            tmp = sizes[i][1]
            sizes[i][1] =sizes[i][0]
            sizes[i][0] = tmp
    ls_1 = []
    ls_2 = []
    
    for s in sizes:
        ls_1.append(s[0])
        ls_2.append(s[1])
    return max(ls_1)*max(ls_2)

        
            
                
        