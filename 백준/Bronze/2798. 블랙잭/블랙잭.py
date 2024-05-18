N, M = map(int, input().split())

lst_2 = []
lst = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = lst[i]+lst[j]+lst[k]
            if sum <= M:
                lst_2.append(sum)

print(max(lst_2))