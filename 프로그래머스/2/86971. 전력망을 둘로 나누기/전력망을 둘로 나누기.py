from collections import deque
ls = []
def solution(n, wires):
    def bfs(start,graph,visited):
        q = deque([start])
        visited[start] = True
        cnt = 1
        while q:
            v = q.popleft()
            for k in graph[v]:
                if not visited[k]:
                    visited[k] = True
                    q.append(k)
                    cnt+=1
        return cnt
   
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if i == j:
                continue
            a = wires[j][0]
            b = wires[j][1]
            graph[a].append(b)
            graph[b].append(a)
        visited = [False]*(n+1)
        
        count = bfs(1,graph,visited)
        ls.append(abs(count-(n-count)))
    return min(ls)
        
        
        
        
            
        