N = int(input())

time = list(map(int, input().split()))
time.sort()

result = time[0]

for i in range(1, len(time)):
    result+=sum(time[:i])+time[i]

print(result)