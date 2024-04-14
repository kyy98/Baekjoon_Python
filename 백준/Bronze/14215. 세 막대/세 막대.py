a, b, c = map(int, input().split())

lst = sorted([a,b,c], reverse=True)

if lst[0] >= lst[1]+lst[2]:
    lst[0] = lst[1]+lst[2]-1
    print(sum(lst))
else:
    print(sum(lst))