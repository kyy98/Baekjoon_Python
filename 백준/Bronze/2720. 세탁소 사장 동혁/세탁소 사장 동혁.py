n= int(input())

for i in range(n):
    C = int(input())
    a = C // 25
    b = C % 25
    c = b // 10
    d = b % 10
    e = d // 5
    f = d % 5
    g = f // 1

    print(a, c, e, g)