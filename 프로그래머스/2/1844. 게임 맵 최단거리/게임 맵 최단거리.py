
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












                