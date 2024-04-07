lst_1=[]
a = int(input())
N = map(int, input().split())
M = list(N)
for i in M:
    lst_2 = [k for k in range(1, i+1) if i % k == 0]
    lst_1.append(lst_2)

lst_3 = [M[j] for j in range(len(M)) if len(lst_1[j])==2]
print(len(lst_3))