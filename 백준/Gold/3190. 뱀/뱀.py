from collections import deque

N = int(input())
K = int(input())

# 1은 벽이나, 몸뚱이
arr = [[1]*(N+2)] + [[1] + [0]*N + [1] for i in range(N)] + [[1]*(N+2)]

for _ in range(K):
    i, j = map(int, input().split())
    arr[i][j] = 2           # 2는 사과

L = int(input())

order = {}
for _ in range(L):
    t, td = input().split()
    order[int(t)] = td

# 현재 신체를 저장하는 리스트
body = deque()
body.append((1, 1))

# 방향 우하좌상 (시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0

t = 0

while True:
    # 매 초 측정
    t += 1

    # 머리 이동
    si, sj = body[-1]    # 신체리스트에 저장된 머리좌표꺼내기
    ni, nj = si+dx[d], sj+dy[d] # 방향만큼 한칸가기


    # 벽이나 몸에 닿으면 종료
    if arr[ni][nj] == 1 or (ni, nj) in body:
        print(t)
        break

    body.append((ni, nj))
    # 사과 만나면 꼬리 복구안함
    if arr[ni][nj] == 2:
        arr[ni][nj] = 0

    # 사과 안만나면 꼬리 줄이기
    elif arr[ni][nj] == 0:
        body.popleft()

    # 다움직이고나서 방향전환
    if t in order.keys():
        if order[t] == 'D':
            d = (d + 1) % 4
        elif order[t] == 'L':
            d = (d - 1) % 4
