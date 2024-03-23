num = int(input())
i = num//4
if num <= 4*i:
    print('long '*i, end='')
    print('int')

elif 4 * i < num <= 4 * (i+1):
    print('long '*(i+1), end='')
    print('int')