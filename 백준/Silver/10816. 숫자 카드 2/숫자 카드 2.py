from bisect import bisect_left, bisect_right
import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

for t in b:
    print(bisect_right(a,t)-bisect_left(a,t), end=' ')