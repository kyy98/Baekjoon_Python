N = int(input())
lst=[]
for i in range(N):
    lst.append(list(map(int,input().split())))

lst = sorted(lst, key=lambda x:(x[1], x[0]))
for j in range(N):
    print(lst[j][0], lst[j][1])