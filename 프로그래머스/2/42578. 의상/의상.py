def solution(clothes):
    dic = {}
    for c in clothes:
        if c[1] not in dic:
            dic[c[1]] = [c[0]]
        else:
            dic[c[1]].append(c[0])
    cnt = 1
    for v in dic.values():
        cnt*=len(v)+1
    return cnt-1
        
            
    
        
    