from itertools import combinations

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

comb = list(combinations(dwarfs, 7))

for c in comb:
    if sum(c) == 100:
        print(*c, sep='\n')
        break
