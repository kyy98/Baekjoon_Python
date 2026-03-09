from collections import deque

def bfs(start, end, graph, visited):
    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v]+1
                q.append(i)
    return visited[end]

n = int(input())
start, end = map(int, input().split())
visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = bfs(start,end,graph,visited)

if result == 0:
    print(-1)
else:
    print(result-1)