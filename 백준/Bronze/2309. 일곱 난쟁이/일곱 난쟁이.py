li = []
for i in range(9):
    row = int(input())
    li.append(row)

for i in li:
    for j in li:
        res = sum(li) - i - j
        if (res == 100) and (i!=j):
            li.remove(i)
            li.remove(j)
li.sort()

for i in li:
    print(i)
