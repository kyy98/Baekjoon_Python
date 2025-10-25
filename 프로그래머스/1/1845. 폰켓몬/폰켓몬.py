def solution(nums):
    dict_n = dict()
    
    for n in nums:
        dict_n[n] = 1
    if len(dict_n) < len(nums)//2:
        return len(dict_n)
    else:
        return len(nums)//2
    