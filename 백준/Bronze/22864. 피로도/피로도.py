a, b, c, m = map(int, input().split())

piro = 0
work = 0

for _ in range(24):
    if piro+a <= m:
        piro+=a
        work+=b
    else:
        if piro-c < 0:
            piro=0
        else:
            piro-=c

print(work)