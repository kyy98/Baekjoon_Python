h, w = map(int, input().split())
cloud = [input() for _ in range(h)]

for c in cloud:
    sky = [-1 for _ in range(w)]
    for i in range(w):
        if c[i] == 'c':
            sky[i] = 0
  
    for j in range(1, w):
        if sky[j-1] != -1 and sky[j] != 0:
            sky[j] = sky[j-1]+1

    print(*sky)