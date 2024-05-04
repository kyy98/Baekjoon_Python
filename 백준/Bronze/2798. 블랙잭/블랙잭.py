a, M = map(int, input().split())

lst = list(map(int, input().split()))

lst_2 = []
for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        for k in range(j+1, len(lst)):
            sum = lst[i]+lst[j]+lst[k]
            if sum > M:
                continue
            else:
                lst_2.append(sum)
            


print(max(lst_2))