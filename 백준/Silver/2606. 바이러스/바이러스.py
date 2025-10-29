def bfs(s):
    q = []
    q.append(s)
    v[s] = 1
  
    while q:
        k = q.pop(0)
        for n in adj[k]:
            if not v[n]:
                q.append(n)
                v[n]=1


N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
v = [0]*(N+1)
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

bfs(1)
print(sum(v)-1)