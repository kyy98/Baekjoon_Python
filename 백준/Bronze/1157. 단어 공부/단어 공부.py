a = input()
a = a.lower()
lst_2=[]
st = set(a)

for k in st:
    cnt = a.count(k)
    lst_1 = [k,cnt]
    lst_2.append(lst_1)

lst_2.sort(key=lambda x: x[1], reverse=True)


if len(lst_2)>=2 and lst_2[0][1] == lst_2[1][1]:
            print('?')
elif len(lst_2)>=2 and lst_2[0][1] != lst_2[1][1]:
    print(lst_2[0][0].upper())
elif len(lst_2) == 1:
    print(lst_2[0][0].upper())