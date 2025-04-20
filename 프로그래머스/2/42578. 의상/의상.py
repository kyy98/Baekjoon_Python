clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


def solution(clothes):
    types = []
    answer = 1
    for i in clothes:
        types.append(i[1])
        types = list(set(types))

    hash_map = {t: 0 for t in types}
    
    for n, t in clothes:
        hash_map[t] += 1
        
        
    if len(hash_map) == 1:
        return next(iter(hash_map.values()))
    else:
        for v in hash_map.values():
            answer *= (v+1)
        return answer-1
solution(clothes)

        
        
        
