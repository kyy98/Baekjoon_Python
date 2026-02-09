from collections import deque

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v]+1
                q.append(i)
    return visited.count(2)+visited.count(3)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1,graph,visited))