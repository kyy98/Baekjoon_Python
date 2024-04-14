a, b = input().split()
b = int(b)
lst = []
alpha_list = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num_list = [i for i in range(36)]

   
for k in a:
    i = alpha_list.index(k)
    j = num_list[i]
    lst.append(j)
lst = lst[::-1]
sum = 0
for i in range(len(lst))[::-1]:
    sum+=lst[i]*(b**i)
print(sum)