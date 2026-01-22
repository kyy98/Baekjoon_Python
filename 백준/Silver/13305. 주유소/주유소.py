n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
result = price[0] * dist[0]

for i in range(1, n-1):
    if price[i-1] < price[i]:
        price[i] = price[i-1]
    result+=price[i]*dist[i]

print(result)