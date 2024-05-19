N = int(input())
lst = []
for i in range(N):
    num = int(input())
    lst.append(num)

lst = sorted(lst)
for j in lst:
    print(j)