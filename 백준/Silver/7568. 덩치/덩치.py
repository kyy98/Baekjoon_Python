n = int(input())
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))

for i in range(n):
    cnt = 1
    for j in range(n):
        if ls[i][0] < ls[j][0] and ls[i][1] < ls[j][1]:
            cnt+=1
    print(cnt, end=' ')