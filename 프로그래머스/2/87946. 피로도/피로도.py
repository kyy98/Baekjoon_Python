from itertools import permutations
def solution(k, dungeons):
    per = list(permutations(dungeons,len(dungeons)))
    ans = []

    for p in per:
        if k >= p[0][0]:
            new_k = k-p[0][1]
            cnt = 1
            for j in range(1,len(p)):
                if new_k >= p[j][0]:
                    new_k-=p[j][1]
                    cnt+=1
                    
        ans.append(cnt)
    return max(ans)