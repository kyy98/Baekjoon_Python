N, M = map(int, input().split())
bsk = [i for i in range(1, N+1)]
temp = 0

for i in range(M):
    a, b = map(int, input().split())
    temp = bsk[a-1]
    bsk[a-1] = bsk[b-1]
    bsk[b-1] = temp
for i in bsk:
    print(i ,end= ' ')