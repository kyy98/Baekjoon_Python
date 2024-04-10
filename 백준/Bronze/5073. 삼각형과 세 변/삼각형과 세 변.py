while True:
    a, b, c = map(int, input().split())
    lst = sorted([a,b,c],reverse=True)
    if lst[0]==lst[1]==lst[2]==0:
        break
    elif lst[0]==lst[1]==lst[2]:
        print('Equilateral')
    elif lst[0]==lst[1]!=lst[2]:
        print('Isosceles')
    elif lst[0] >= lst[1]+lst[2]:
        print('Invalid')
    elif lst[0]!=lst[1]==lst[2] or lst[0]==lst[2]!=lst[1]:
        print('Isosceles')
    elif lst[0]!=lst[1]!=lst[2]:
        print('Scalene')