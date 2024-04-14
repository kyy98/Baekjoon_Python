a, b = input().split()
b = int(b)
a = list(a)[::-1]

alpha_list = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")

sum = 0
for i in range(len(a))[::-1]:
    sum+=alpha_list.index(a[i])*(b**i)
print(sum)