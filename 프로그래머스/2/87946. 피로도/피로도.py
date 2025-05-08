from itertools import permutations

# def solution(k, dungeons):
    # max_cnt = 0
    # for perm in permutations(dungeons, len(dungeons)):
    #     cnt = 0
    #     cur_k = k
    #     for min, consume in perm:
    #         if cur_k >= min:
    #             cur_k-=consume
    #             cnt+=1
    #         else:
    #             break
    #     max_cnt = max(max_cnt, cnt)
    # return max_cnt
     
        
        
from itertools import permutations
def solution(k, dungeons):
    p = list(permutations(dungeons, len(dungeons)))
    ls = []
    for d in p:
        cur_k = k
        cnt = 0
        for i in range(len(d)):
            if cur_k >= d[i][0]:
                cur_k-=d[i][1]
                cnt+=1
            ls.append(cnt)
    max_score = max(ls)
    return max_score
            
    
    

              

            
                
    
                