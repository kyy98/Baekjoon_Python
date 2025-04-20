nums = [3,1,2,3]
def solution(nums):
    ls = list(set(nums))
    if len(ls) >= len(nums)/2:
        return len(nums)/2
    else:
        return len(ls)
solution(nums)