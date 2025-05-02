from itertools import permutations
import math
numbers = "17"

def sosu(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

def solution(numbers):
    answer = 0
    p = []
    result = []
    cnt = 0
    
    for i in range(1, len(numbers)+1):
        p.extend(permutations(numbers, i))
        result = [''.join(k) for k in p]
        result = list(set([int(k) for k in result]))
    for j in result:
        if sosu(j):
            cnt+=1
    return cnt
        
solution(numbers)
    
        