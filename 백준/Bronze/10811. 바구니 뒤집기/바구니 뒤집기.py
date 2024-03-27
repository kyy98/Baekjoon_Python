N, M = map(int, input().split())
bsk = [i for i in range(1, N+1)]
for i in range(M):
    a, b = map(int, input().split())
    temp = bsk[a-1:b]
    bsk[a-1:b] = reversed(temp)
        
for i in bsk:
    print(i, end=' ')