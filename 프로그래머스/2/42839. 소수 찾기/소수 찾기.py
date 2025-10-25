from itertools import permutations

ls_1 = []
ls_2 = []
def solution(numbers):
    for n in numbers:
        ls_1.append(n)
    for i in range(1, len(ls_1)+1):
        for p in permutations(ls_1, i):
            num = ''.join(p)
            ls_2.append(num)
    ls_3 = list(set(ls_2))
    ls_3 = [num for num in ls_3 if num[0] != '0' and num != '1']
    
    sosu = []

    for num in ls_3:
        if all(int(num) % i != 0 for i in range(2, int(num))):
            sosu.append(num)
                  
    return len(sosu)
            
            
            
            
        
    