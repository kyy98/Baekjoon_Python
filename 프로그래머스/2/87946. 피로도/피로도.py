from itertools import permutations
def solution(k, dungeons):
    ls = []
    for p in permutations(dungeons, len(dungeons)):
        cnt = 0
        temp_k = k
        for i in range(len(dungeons)):
            if temp_k >= p[i][0]:
                cnt+=1
                temp_k-=p[i][1]
            ls.append(cnt)
                
            
    return max(ls)
    
            
            
        
        