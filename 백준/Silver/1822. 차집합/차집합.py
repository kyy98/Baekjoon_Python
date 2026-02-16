import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

b.sort()

def binary_search(target, start, end):
    while (start<=end):
        mid=(start+end)//2
        if b[mid] == target:
            return True
        elif b[mid] > target:
            end=mid-1
        else:
            start=mid+1
    return False

ans = []
for t in a:
    if not binary_search(t,0,m-1):
        ans.append(t)
ans.sort()
print(len(ans))
print(*ans, sep=' ')