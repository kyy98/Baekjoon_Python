def solution(n, computers):
    def bfs(s):
        q = []
        q.append(s)
        v[s] = 1
        
        while q:
            c = q.pop(0)
            for i in range(n):
                if computers[c][i] == 1 and not v[i]:
                    q.append(i)
                    v[i] = 1
    
    
    v = [0]*n
    cnt = 0
    for i in range(n):
        if not v[i]:
            bfs(i)
            cnt+=1
    return cnt
    
        
                

            

    
