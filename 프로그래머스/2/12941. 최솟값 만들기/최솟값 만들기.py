from itertools import product
def solution(A,B):
    result = 0
    list_A = sorted(A)
    list_B = sorted(B, reverse=True)
    for i in range(len(A)):
        result+=list_A[i]*list_B[i]
       

    return result