lst = []
for i in range(10):
    a = input()
    lst.append(int(a))

b = list(map(lambda x: x % 42, lst))
c = set(b)
print(len(c))