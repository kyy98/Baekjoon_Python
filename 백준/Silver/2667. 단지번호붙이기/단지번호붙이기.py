from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ls = []

def bfs(x,y):
    q = deque([])
    q.append((x,y))
    graph[x][y] = 0
    cnt_2 = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<=-1 or nx>=n or ny<=-1 or ny>=n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt_2+=1
    ls.append(cnt_2)

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

cnt_1 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
            cnt_1+=1

print(cnt_1, end='\n')
ls.sort()
print(*ls, sep='\n')