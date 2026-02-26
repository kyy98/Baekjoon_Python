import sys
input = sys.stdin.readline

n,m = map(int, input().split())
array = [0]+list(map(int, input().split()))
dp = [0]*(n+1)

for k in range(1, n+1):
    dp[k] = dp[k-1]+array[k]

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j]-dp[i-1])