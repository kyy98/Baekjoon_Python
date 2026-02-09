from collections import deque

def bfs(x,y,z,w):
    q = deque([])
    q.append((x,y))
    graph[x][y] = 1

    while q:
        x,y = q.popleft()
        for p in range(8):
            nx = x+dx[p]
            ny = y+dy[p]
            if nx<0 or nx>=i or ny<0 or ny>=i:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))
                if (nx,ny) == (z,w):
                    break
    return graph[z][w]-1

t = int(input())
for _ in range(t):
    i = int(input())
    graph = [[0]*i for k in range(i)]
    ci, cj = map(int, input().split())
    ei, ej = map(int, input().split())

    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [-1,-2,-2,-1,1,2,2,1]

    print(bfs(ci,cj,ei,ej))