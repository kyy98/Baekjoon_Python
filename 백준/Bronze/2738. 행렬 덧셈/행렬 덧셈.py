N, M = map(int, input().split())

lst_1, lst_2 = [], []

for i in range(N):
    a = list(map(int, input().split()))
    lst_1.append(a)

for j in range(N):
    b = list(map(int, input().split()))
    lst_2.append(b)

for i in range(N):
    for j in range(M):
        print(lst_1[i][j]+lst_2[i][j], end=' ')
    print()