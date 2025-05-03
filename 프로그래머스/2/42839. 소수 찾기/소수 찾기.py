from itertools import permutations
import math

def sosu(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

def solution(numbers):
    cnt = 0
    p = []
    for i in range(1, len(numbers)+1):
        p.extend(permutations(numbers, i))
    perm = list(int(''.join(k)) for k in p)
    for i in set(perm):
        if sosu(i):
            cnt+=1
    return cnt
            

    
        