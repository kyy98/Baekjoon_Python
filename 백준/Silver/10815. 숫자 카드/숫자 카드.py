N = int(input())
set_1 = set(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))

for i in lst:
    if i in set_1:
        print(1, end=' ')
    else:
        print(0, end=' ')
