def solution(maps):
    def bfs(si, sj):
        N = len(maps)
        M = len(maps[0])
        q = []
        v = [[0]*M for _ in range(N)]
        
        q.append((si,sj))
        v[si][sj]=1
        
        while q:
            ci, cj = q.pop(0)
            if (ci,cj) == (N-1,M-1):
                return v[N-1][M-1]
            
            for di, dj in ((-1,0),(0,-1),(1,0),(0,1)):
                ni, nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<M and maps[ni][nj]==1 and v[ni][nj]==0:
                    q.append((ni,nj))
                    v[ni][nj]=v[ci][cj]+1
        return -1
    return bfs(0,0)