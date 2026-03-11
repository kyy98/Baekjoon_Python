from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = []
def bfs(x,y):
    q = deque([])
    q.append((x,y))
    graph[x][y] = 1
    cnt_2 = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx,ny))
                cnt_2+=1
    ans.append(cnt_2)

m,n,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]

for _ in range(k):
    a,b,c,d = map(int, input().split())
    for i in range(a,c):
        for j in range(b,d):
            graph[i][j] = 1
cnt_1 = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i,j)
            cnt_1+=1
print(cnt_1)
ans.sort()
print(*ans)