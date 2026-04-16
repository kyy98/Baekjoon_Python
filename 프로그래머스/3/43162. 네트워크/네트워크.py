from collections import deque

def solution(n, computers):
    visited = [0]*n
    
    def bfs(s):
        q = deque([])
        q.append(s)
        
        while q:
            v = q.popleft()
            for i in range(n):
                if computers[v][i] == 1 and not visited[i]:
                    visited[i] = 1
                    q.append(i)
    cnt = 0  
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt+=1
    return cnt