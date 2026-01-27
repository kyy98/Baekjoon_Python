n = int(input())
dic = {}
cnt = 0

for _ in range(n):
    cow, pos = input().split()
    if cow in dic:
        if dic[cow] != pos:
            dic[cow] = pos
            cnt+=1
    else:
        dic[cow] = pos

print(cnt)