b = []
for i in range(9):
    a = input()
    b.append(int(a))
print(max(b))
print(b.index(max(b))+1)