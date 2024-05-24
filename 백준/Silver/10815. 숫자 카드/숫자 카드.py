N = int(input())
lst_1 = list(map(int, input().split()))
M = int(input())
lst_2 = list(map(int, input().split()))
dic = {}

for i in lst_2:
    dic[i] = 0

for j in lst_1:
    if j in dic:
        dic[j] = 1

for i in dic:
    print(dic[i], end=' ')
