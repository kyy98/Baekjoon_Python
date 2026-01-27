n, m = map(int, input().split())
light = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        light[b-1] = c
    elif a == 2: 
        for i in range(b-1, c):
            if light[i] == 0:
                light[i] = 1
            else:
                light[i] = 0
    elif a == 3:
        for i in range(b-1,c):
            light[i] = 0
    else:
        for i in range(b-1, c):
            light[i] = 1

for l in light:
    print(l, end=' ')