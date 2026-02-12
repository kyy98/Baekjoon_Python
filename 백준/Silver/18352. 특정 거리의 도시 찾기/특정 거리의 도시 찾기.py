from collections import deque
import sys
from collections import deque

# 이 줄을 추가하면 입력 속도가 압도적으로 빨라집니다.
input = sys.stdin.readline

answer = []

def bfs(start,graph,visited):
    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v]+1
                if visited[i] == (k+1):
                    answer.append(i)
                q.append(i)


n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    
visited = [0]*(n+1)

bfs(x,graph,visited)

if len(answer) > 0:
    answer.sort()
    print(*answer)
else:
    print(-1)