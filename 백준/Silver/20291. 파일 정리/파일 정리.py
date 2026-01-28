from collections import Counter
n = int(input())
ls = []
for _ in range(n):
    name, file = input().split('.')
    ls.append(file)
ls.sort()
for key, value in dict(Counter(ls)).items():
    print(key, value)