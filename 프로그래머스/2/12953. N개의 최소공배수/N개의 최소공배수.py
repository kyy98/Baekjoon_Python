# #최소공배수
# def lcm(a, b):
#     return (a * b) // gcd(a, b)

from math import gcd
def solution(arr):
    total = arr[0]
    
    for i in arr[1:]:
        total = (total*i) // gcd(total, i)  
    
    return total
        
        
        
            