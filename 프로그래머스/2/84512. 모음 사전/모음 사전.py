from itertools import product

def solution(word):
    result = []
    for i in range(1, 6):
        ls = list(product(["A", "E", "I", "O", "U"], repeat=i))
        for j in ls:
            result.append(''.join(j))
    result = sorted(result)
    return result.index(word)+1
            
            