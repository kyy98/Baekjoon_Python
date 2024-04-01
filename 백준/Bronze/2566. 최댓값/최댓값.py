lst = []
lst_2 = []
for i in range(9):
  a = list(map(int, input().split()))
  lst.append(a)
for i in range(9):
  for j in range(9):
    lst_2.append(lst[i][j])
print(max(lst_2))
lst_3 = [(i, j) for i in range(9) for j in range(9) if lst[i][j] == max(lst_2)]
for i, j in lst_3:
  print(i+1, j+1, end=' ')