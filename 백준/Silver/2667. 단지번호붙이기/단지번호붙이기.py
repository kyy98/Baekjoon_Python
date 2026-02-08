def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        global ans
        ans+=1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        return True
    return False

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

cnt = 0
ans = 0
ls = []
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            cnt+=1
            ls.append(ans)
            ans = 0

ls.sort()
print(cnt, end='\n')
print(*ls, sep='\n')
