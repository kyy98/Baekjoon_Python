from itertools import permutations

def solution(numbers):
    nums = []
    for i in numbers:
        nums.append(i)
    per = []
    for i in range(1, len(nums)+1):
        for p in permutations(nums, i):
            per.append(''.join(p))
            
    per_2 = list(set(list(map(int,per))))
    cnt = len(per_2)
    for i in per_2:
        if i<2:
            cnt-=1
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                cnt-=1
                break
    return cnt
            
        
        
    