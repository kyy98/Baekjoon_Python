num = int(input())
lst_1, lst_2 = [], []
if num == 1:
    x1, y1 = map(int, input().split())
    print(0)
    
else:
    for i in range(num):
        x1, y1 = map(int, input().split())
        lst_x = x1
        lst_y = y1
        lst_1.append(lst_x)
        lst_2.append(lst_y)
    x = max(lst_1)-min(lst_1)
    y = max(lst_2)-min(lst_2)
    print(x*y)