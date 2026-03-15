n = int(input())
array = list(map(int, input().split()))
array_2 = [0]*n
m = int(input())
array.sort()
start = 1
end = max(array)
while start<=end:
    mid = (start+end)//2
    for i in range(n):
        array_2[i] = min(array[i],mid)
    if sum(array_2) > m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)