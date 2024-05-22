N = int(input())
lst=[]
for i in range(N):
    x, y = map(int,input().split())
    lst.append([x,y])
lst.sort()
for k in range (len(lst)):
    print(lst[k][0], lst[k][1])