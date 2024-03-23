lst = []
for i in range(28):
    a = input()
    lst.append(int(a))

b = [i for i in range(1, 31)]
k = [i for i in b if i not in lst]

for i in k:
    print(i)