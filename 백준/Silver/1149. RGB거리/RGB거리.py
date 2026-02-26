n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(n)]
dp[0][0] = array[0][0]
dp[0][1] = array[0][1]
dp[0][2] = array[0][2]

for i in range(1, n):
    dp[i][0] = min(array[i][0]+dp[i-1][1], array[i][0]+dp[i-1][2])
    dp[i][1] = min(array[i][1]+dp[i-1][0], array[i][1]+dp[i-1][2])
    dp[i][2] = min(array[i][2]+dp[i-1][0], array[i][2]+dp[i-1][1])

print(min(dp[n-1]))  