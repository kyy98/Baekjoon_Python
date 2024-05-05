N = int(input())
lst=[]
for i in range(1,N):
    if sum(map(int, str(i)))+i == N:
        lst.append(i)
if lst == []:
    print(0)
else:
    print(min(lst))