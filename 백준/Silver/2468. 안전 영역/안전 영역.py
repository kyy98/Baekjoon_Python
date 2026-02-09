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

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny)) 


region = []
n = int(input())

for _ in range(n):
    region.append(list(map(int, input().split())))

unique = set()
for arr in region:
    for x in arr:
        unique.add(x)

graph = [[0]*n for _ in range(n)]
result = [1]
for u in unique:
    for i in range(n):
        for j in range(n):
            if region[i][j] > u:
                graph[i][j] = 1
    cnt=0
    for k in range(n):
        for j in range(n):
            if graph[k][j] == 1:
                bfs(k,j)
                cnt+=1
                result.append(cnt)

print(max(result))