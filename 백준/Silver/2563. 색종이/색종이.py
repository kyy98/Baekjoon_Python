N = int(input())
cnt = 0
w_paper = [[0 for j in range(100)] for i in range(100)]

for i in range(N):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            w_paper[j][k] = 1

for i in range(100):
    for j in range(100):
        if w_paper[i][j] == 1:
            cnt+=1

print(cnt) 