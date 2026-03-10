from collections import deque
array = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

def bfs(sx,sy,ex,ey):
    q = deque([])
    q.append((sx,sy))
    graph[sx][sy] = 1
  
    while q:
        x,y = q.popleft()
        for i in range(len(array)):
            dx = x+array[i][0]
            dy = y+array[i][1]

            if dx<0 or dx>=l or dy<0 or dy>=l:
                continue
            if graph[dx][dy] == 0:
                graph[dx][dy] = graph[x][y]+1
                q.append((dx,dy))
    return graph[ex][ey]-1

t = int(input())
for _ in range(t):
    l = int(input())
    s_x,s_y = map(int, input().split())
    e_x,e_y = map(int, input().split())
    graph = [[0]*l for _ in range(l)]
    print(bfs(s_x,s_y,e_x,e_y))