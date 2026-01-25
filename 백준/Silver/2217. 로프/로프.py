n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

ls = []

for i in range(n):
    ls.append(rope[i]*(i+1))

print(max(ls))