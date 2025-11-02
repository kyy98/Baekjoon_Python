def solution(n, computers):
    def bfs(s):
        q = []
        q.append(s)
        v[s] = 1
        
        while q:
            k = q.pop(0)
            for i in range(n):
                if computers[k][i]==1 and v[i] == 0:
                    q.append(i)
                    v[i] = 1
    
    v = [0]*n
    answer = 0
    for i in range(n):
        if not v[i]:
            bfs(i)
            answer+=1
    return answer