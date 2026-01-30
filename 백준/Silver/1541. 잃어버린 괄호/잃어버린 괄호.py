s = input()
ls = s.split('-')

num = sum(map(int, ls[0].split('+')))

for i in range(1, len(ls)):
    ls[i] = sum(map(int, ls[i].split('+')))
    num-=ls[i]

print(num)