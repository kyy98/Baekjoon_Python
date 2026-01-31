n = int(input())

for _ in range(n):
    k = int(input())
    n = int(input())

    ls = [i for i in range(1, n+1)]

    for _ in range(k):
        for i in range(1, n):
            ls[i]+=ls[i-1]
  
    print(ls[-1])