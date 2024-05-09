n = int(input())
lst = list(map(int, input().split()))
nums = sorted(lst)
target = int(input())
start = 0
end = len(nums)-1
count = 0

while start != end:
    if nums[start]+nums[end] > target:
        end-=1
    elif nums[start]+nums[end] < target:
        start+=1
    elif nums[start]+nums[end] == target:
        count+=1
        start+=1

print(count) 