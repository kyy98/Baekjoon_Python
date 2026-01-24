n = int(input())
num = list(map(int, input().split()))

result = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if result[j] == 0:
            cnt+=1
            if cnt == num[i]+1:
                result[j] = i+1
                break

print(*result)