n, l = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()

for i in ls:
    if l < i:
        break
    l+=1

print(l)