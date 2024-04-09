a,b = map(int, input().split())
c,d = map(int, input().split())
e,f = map(int, input().split())

lst_1 = [a,c,e]
lst_2 = [b,d,f]

for i in lst_1:
    if lst_1.count(i) == 1:
        x = i
for i in lst_2:
    if lst_2.count(i) == 1:
        y = i

print(x,y)