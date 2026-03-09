from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque([])
    q.append((x,y))
    graph[x][y] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0

t = int(input())

for c in range(t):
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt+=1
    print(cnt)