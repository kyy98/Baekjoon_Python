N = int(input())
cnt = N
for i in range(N):
    w = input()
    for j in range(len(w)-1):
        if w[j] == w[j+1]:
            pass
        if w[j] != w[j+1] and w[j] in w[j+2:]:
            cnt-=1
            break

print(cnt)