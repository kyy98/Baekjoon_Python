n,m = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(start, end, target):
    res = 0
    while start <= end:
        result = 0
        mid = (start+end)//2
        for x in array:
            if x > mid:
                result+=x-mid
        if result < target:
            end = mid-1
        else:
            res = mid
            start = mid+1
    return res

print(binary_search(0,max(array),m))


