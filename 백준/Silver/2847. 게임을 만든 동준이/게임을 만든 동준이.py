N = int(input())

ls = []
for i in range(N):
    a = int(input())
    ls.append(a)

result = 0
for i in range(len(ls)-1, 0, -1):
    if ls[i] <= ls[i-1]:
        result+=ls[i-1]-(ls[i]-1)
        ls[i-1] = ls[i]-1

print(result)