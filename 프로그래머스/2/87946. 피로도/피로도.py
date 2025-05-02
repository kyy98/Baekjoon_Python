from itertools import permutations

def solution(k, dungeons):
    max_cnt = 0
    for perm in permutations(dungeons, len(dungeons)):
        cur_k = k
        cnt = 0
        for minimum, consume in perm:
            if cur_k >= minimum:
                cur_k -= consume
                cnt += 1
            else:
                break
        max_cnt = max(max_cnt, cnt)
    return max_cnt

                

              

            
                
    
                