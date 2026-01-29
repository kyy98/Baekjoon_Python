n = int(input())
cnt = n

for _ in range(n):
    word = input()
    ls = [word[0]]
    for s in word[1:]:
        if (ls[-1] != s) and (s in ls):
            cnt-=1
            break
        ls.append(s)

print(cnt)