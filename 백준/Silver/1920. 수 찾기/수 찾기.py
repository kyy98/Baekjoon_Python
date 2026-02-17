import sys
input = sys.stdin.readline

n = int(input())
arr_1 = list(map(int, input().split()))
m = int(input())
arr_2 = list(map(int, input().split()))

arr_1.sort()

def binary_s(start, end, target):
    while (start<=end):
        mid = (start+end)//2
        if arr_1[mid] == target:
            return True
        elif arr_1[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return False

for t in arr_2:
    if binary_s(0,n-1,t):
        print(1)
    else:
        print(0)