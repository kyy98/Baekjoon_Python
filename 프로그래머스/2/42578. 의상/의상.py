def solution(clothes):
    dict = {}
    num = 1
    for c in clothes:
        if c[1] not in dict:
            dict[c[1]] = [c[0]]
        else:
            dict[c[1]] += [c[0]]
    for v in dict.values():
        num *= len(v)+1
    return num-1
        
    