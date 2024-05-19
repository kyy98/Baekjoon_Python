N = str(input())
lst = []
for i in N:
    lst.append(int(i))
for j in sorted(lst, reverse=True):
    print(j, end='')