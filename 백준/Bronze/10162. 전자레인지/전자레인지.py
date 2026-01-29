n = int(input())
time = [300, 60, 10]
number=[]

for t in time:
    number.append(n//t)
    n%=t

if n == 0:
    print(*number)
else:
    print(-1)