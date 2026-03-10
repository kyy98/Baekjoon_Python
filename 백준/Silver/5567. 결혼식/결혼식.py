from collections import deque
n = int(input())
m = int(input())

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v]+1
                q.append(i)
    return visited.count(1)+visited.count(2)


graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(1,graph,visited))