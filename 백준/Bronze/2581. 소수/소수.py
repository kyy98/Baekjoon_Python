lst_1 = []
M = int(input())
N = int(input())
lst_2 = [i for i in range(M, N+1)]
for i in range(M, N+1):
    lst_3 = [k for k in range(1, i+1) if i % k == 0]
    lst_1.append(lst_3)
lst_4 = [lst_2[i] for i in range(len(lst_2)) if len(lst_1[i]) == 2]
if sum(lst_4) == 0:
    print(-1)
else:
    print(sum(lst_4))
    print(min(lst_4))