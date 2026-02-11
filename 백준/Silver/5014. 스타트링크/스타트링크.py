from collections import deque


def bfs(start, visited):
    if start == g:
        return 0
    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()
        for i in [v+u, v-d]:
            if i < 1 or i > f:
                continue
            if visited[i] == 0:
                visited[i] = visited[v]+1
                q.append(i)
            if i == g:
                return visited[g]-1
    return "use the stairs"
f,s,g,u,d = map(int, input().split())
visited = [0]*(f+1)

print(bfs(s,visited))
