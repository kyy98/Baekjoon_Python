number = input()

if '0' not in number:
    print(-1)

else:
    ls_1 = [int(n) for n in number]
    if sum(ls_1) % 3 == 0:
        ls_2 = sorted(ls_1, reverse=True)
        print(''.join(map(str, ls_2)))
    else:
        print(-1)