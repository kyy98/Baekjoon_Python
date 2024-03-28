num = int(input())
for i in range(num):
    R, a = input().split()
    for j in a:
        print(j*int(R), end='')
    print()