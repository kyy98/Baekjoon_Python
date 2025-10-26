from itertools import product
def solution(word):
    moeum = ['A', 'E', 'I', 'O', 'U']
    ls = []
    for i in range(1, 6):
        for p in product(moeum, repeat=i):
            w = ''.join(p)
            ls.append(w)
    ls = sorted(ls)
    return ls.index(word)+1