N = int(input())
lst = []
for i in range(N):
    w = input()
    lst.append(w)
lst = set(lst)
lst = sorted(lst, key=lambda x: (len(x), x))

for j in lst:
    print(j)