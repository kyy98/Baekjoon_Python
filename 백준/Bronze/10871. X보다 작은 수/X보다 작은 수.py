N ,X = map(int, input().split())
a = map(int, input().split())
b = list(a)
for i in b:
    if i < X:
        print(i, end=' ')