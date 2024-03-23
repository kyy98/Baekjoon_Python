lst = []
for i in range(10):
    a = input()
    lst.append(int(a))

b = [i % 42 for i in lst]
c = set(b)
print(len(c))
