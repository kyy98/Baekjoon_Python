def bfs(s):
    q = []
    q.append(s)
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]:
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1
    return len(ans_bfs)-1





N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
v = [0]*(N+1)
ans_bfs = []
for i in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

print(bfs(1))
