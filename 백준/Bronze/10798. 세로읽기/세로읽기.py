lst=[]
for i in range(5):
    n = list(input())
    lst.append(n)
for i in range(15):
    for j in range(5):
        if i < len(lst[j]):
            print(lst[j][i], end='')