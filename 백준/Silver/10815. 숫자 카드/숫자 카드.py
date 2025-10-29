N = int(input())
ls_1 = set(map(int, input().split()))
M = int(input())
ls_2 = list(map(int, input().split()))

for i in range(M):
    if ls_2[i] in ls_1:
        ls_2[i] = 1
    else:
        ls_2[i] = 0
for j in ls_2:
      print(j, end=' ')
