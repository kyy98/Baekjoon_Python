def solution(maps):
    N = len(maps)
    M = len(maps[0])
    ls = []
    
    def bfs(si, sj, N, M):
        q = []
        v = [[0]*M for _ in range(N)]
        cnt = 0
        
        q.append((si,sj))
        v[si][sj] = 1
        
        while q:
            ci, cj = q.popleft()
            for di, dj in ((-1,0),(0,-1), (0,1), (1,0)):
                ni, nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<M and maps[ni][nj]==1 and v[ni][nj]==0:
                    q.append((ni,nj))
                    v[ni][nj] = 1
                    cnt+=1
        ls.append(cnt)
        if ls:
            return min(ls)
        else:
            return -1











# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
    
#     def bfs(si, sj):
#         q = []
#         q.append((si,sj))
#         v[si][sj] = 1
        
#         while q:
#             ci, cj = q.pop(0)
#             if (ci, cj) == (n-1, m-1):
#                 return v[n-1][m-1]
#             for di, dj in ((-1,0), (0,-1), (1,0), (0,1)):
#                 ni, nj = ci+di, cj+dj
#                 if 0<=ni<n and 0<=nj<m and v[ni][nj]==0 and maps[ni][nj]==1:
#                     q.append((ni,nj))
#                     v[ni][nj] = v[ci][cj]+1
#         return -1
                
#     v = [[0]*m for _ in range(n)]
#     return bfs(0,0)


def solution(maps):
    def bfs(si, sj):
        q = []
        q.append((si, sj))
        v[si][sj] = 1
        
        while q:
            ci, cj = q.pop(0)
            if (ci, cj) == (n-1, m-1):
                return v[n-1][m-1]
            for di, dj in ((-1,0),(0,-1),(1,0),(0,1)):
                ni, nj = ci+di, cj+dj
                if 0<=ni<n and 0<=nj<m and maps[ni][nj]==1 and not v[ni][nj]:
                    q.append((ni,nj))
                    v[ni][nj] = v[ci][cj]+1
        return -1
    
    n = len(maps)
    m = len(maps[0])
    v = [[0]*m for _ in range(n)]
                
    return bfs(0,0)












                