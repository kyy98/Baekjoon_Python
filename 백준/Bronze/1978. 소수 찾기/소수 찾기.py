import sys

N = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in li:
    if i == 1:
        continue
    elif i <= 3:
        cnt += 1
    else:
        n = 0
        for j in range(2, i):
            if i % j == 0:
                n += 1
                break
        if n == 0:
            cnt += 1

print(cnt)

