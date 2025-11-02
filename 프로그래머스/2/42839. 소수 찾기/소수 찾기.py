from itertools import permutations

def solution(numbers):
    nums = list(numbers)
    all_nums = set()
    
    for i in range(1, len(nums)+1):
        for p in permutations(nums, i):
            all_nums.add(int(''.join(p)))
            
    primes = []
    for n in all_nums:
        if n>1 and all(n%i!=0 for i in range(2, int(n**0.5)+1)):
            primes.append(n)
    return len(primes)
        
    