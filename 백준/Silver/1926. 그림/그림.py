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
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt+=1
                q.append((nx,ny))
    ls.append(cnt)

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i,j)
            answer+=1

print(answer)
print(max(ls) if ls else 0)