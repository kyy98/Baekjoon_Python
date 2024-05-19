lst = []
for i in range(5):
    num = int(input())
    lst.append(num)
lst = sorted(lst)
print(sum(lst)//5)
print(lst[2])