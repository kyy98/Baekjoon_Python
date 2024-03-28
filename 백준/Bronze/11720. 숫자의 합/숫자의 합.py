a = int(input())
b = input()
lst=[]
for i in range(a):
    lst.append(b[i])
lst = map(int, lst)
print(sum(lst))