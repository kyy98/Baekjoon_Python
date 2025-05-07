# from itertools import permutations
# import math

# def sosu(n):
#     if n < 2:
#         return False
#     else:
#         for i in range(2, int(math.sqrt(n)+1)):
#             if n % i == 0:
#                 return False
#         return True

# def solution(numbers):
#     cnt = 0
#     p = []
#     for i in range(1, len(numbers)+1):
#         p.extend(permutations(numbers, i))
#     perm = list(int(''.join(k)) for k in p)
#     for i in set(perm):
#         if sosu(i):
#             cnt+=1
#     return cnt
            
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
    ls = []
    for i in range(1, len(numbers)+1):
        ls.extend(permutations(numbers, i))    # permutations 결과 list에 넣어줘야 함
    
    for i in range(len(ls)):
        ls[i] = int(''.join(ls[i]))
    
    
    cnt = 0
    ls = list(set(ls))
    for i in ls:
        if sosu(i):
            cnt+=1
    return cnt
        
    
    
    
    
    
    
    
    
    
    
    
    
        