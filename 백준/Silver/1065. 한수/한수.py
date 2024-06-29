N = int(input())
lst = []
for i in range(1, N+1):
    if len(str(i)) == 1 or len(str(i)) == 2:
        lst.append(i)
    else:
        if int(str(i)[2])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[0]):
            lst.append(i)
print(len(lst))