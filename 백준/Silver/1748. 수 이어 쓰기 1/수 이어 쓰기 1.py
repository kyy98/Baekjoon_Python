n = int(input())
l = len(str(n))
num = 0

for i in range(l-1):
    num+=(i+1)*(9*(10**i))

num+=l*(n-10**(l-1)+1)
print(num)