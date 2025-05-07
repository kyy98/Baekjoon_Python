def solution(n, computers):
    def bfs(i):
        q=[]
        q.append(i)
        visited[i] = True
        while q:
            c = q.pop(0)
            for j in range(n):
                if not visited[j] and computers[j][c]:
                    q.append(j)
                    visited[j] = True    
    
    visited = [False] * n
    cnt = 0       
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
        
    return cnt
