import sys
# 재귀 깊이 제한 설정 (필수)
sys.setrecursionlimit(10000)

def dfs(x,y):
    if x<0 or x>=m or y<0 or y>=n:
        return False
  
    if graph[y][x] == 1:
        graph[y][x] = 0

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        return True
    return False

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for p in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                cnt+=1
    print(cnt)