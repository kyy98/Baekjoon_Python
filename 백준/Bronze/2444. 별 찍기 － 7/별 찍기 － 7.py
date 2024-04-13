num = int(input())

for i in range(num):
    print(' '*(num-(i+1)), end='')
    print('*'*(2*i+1))

for j in range(num-1):
    print(' '*(j+1), end='')
    print('*'*(2*((num-1)-(j+1))+1))