def solution(sizes):
    ls_1 = []
    ls_2 = []
    for i in sizes:
        ls_1.append(i[0])
        ls_2.append(i[1])
        
    if max(ls_1) > max(ls_2):
        for s in sizes:
            if s[0] < s[1]:
                s[0], s[1] = s[1], s[0]
        ls_3 = []
        for i in sizes:
            ls_3.append(i[1])
        return max(ls_1)*max(ls_3)
    else:
        for s in sizes:
            if s[0] > s[1]:
                s[0], s[1] = s[1], s[0]
        ls_4 = []
        for i in sizes:
            ls_4.append(i[0])
        return max(ls_4)*max(ls_2)
    return max(ls_1)*max(ls_2)
        
        

        
            
                
        