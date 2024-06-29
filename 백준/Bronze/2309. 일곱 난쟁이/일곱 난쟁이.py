lst = []
for i in range(9):
    height = int(input())
    lst.append(height)

for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        s = lst[i]+lst[j]
        if 100 == sum(lst)-s:
            a,b = lst[i], lst[j]
lst.remove(a)
lst.remove(b)

for i in sorted(lst):
    print(i)