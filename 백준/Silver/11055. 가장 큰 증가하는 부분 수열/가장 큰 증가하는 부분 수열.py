n = int(input())
array = list(map(int, input().split()))
d = array[:]

for i in range(1,n):
    for j in range(0,i):
        if array[j]<array[i]:
            d[i] = max(d[i], d[j]+array[i])
      
print(max(d))
