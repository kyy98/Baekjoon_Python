from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ls = []

def bfs(x,y):
    q = deque([])
    q.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt+=1
                q.append((nx,ny))
    ls.append(cnt)

m,n,k = map(int, input().split())

graph = [[1]*n for _ in range(m)]

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for y in range(ly,ry):
        for x in range(lx,rx):
            graph[y][x] = 0

count = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
            count+=1

print(count)
ls.sort()
print(*ls, end=' ')