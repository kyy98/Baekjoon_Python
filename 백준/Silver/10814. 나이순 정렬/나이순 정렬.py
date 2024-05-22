N = int(input())
lst=[]
for i in range(N):
    x, y = input().split()
    lst.append([int(x), y])
lst = sorted(lst, key=lambda x:x[0])
for j in range(N):
    print(lst[j][0], lst[j][1])