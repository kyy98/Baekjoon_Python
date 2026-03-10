from collections import deque

s, e = map(int, input().split())
graph = [0]*100001

def bfs(start,end):
    q = deque([start])
    graph[start] = 1

    while q:
        v = q.popleft()
        for i in [v-1,v+1,v*2]:
            if i<0 or i>100000:
                continue
            if graph[i] == 0:
                graph[i] = graph[v]+1
                q.append(i)
            if (i==end):
                return graph[end]-1

print(bfs(s,e))