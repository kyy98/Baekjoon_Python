from collections import deque

n = int(input())
a,b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0]*(n+1)

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v]+1
                if i == b:
                    return visited[i]-1
                    break
                q.append(i)
    return -1

print(bfs(a,graph,visited))
    
