N, M = map(int, input().split())
lst_1, lst_2 = [], []
cnt = 0

for i in range(N):
    w = input()
    lst_1.append(w)
set_1 = set(lst_1)

for j in range(M):
    a = input()
    lst_2.append(a)

for k in lst_2:
    if k in set_1:
        cnt+=1

print(cnt)