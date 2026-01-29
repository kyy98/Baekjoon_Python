n = int(input())
answer = 0
length = len(str(n))

for d in range(1, length):
    answer+=9*(10**(d-1))*d

answer+=(n-(10**(length-1))+1)*length
print(answer)