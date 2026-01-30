n, m = map(int, input().split())

ls = list(map(int, input().split()))
ls.sort()

for _ in range(m):
    num = ls[0]+ls[1]
    ls[0], ls[1] = num, num
    ls.sort()

print(sum(ls))