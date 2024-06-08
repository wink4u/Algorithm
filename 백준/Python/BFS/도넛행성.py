import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

donut = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx == -1:
                nx = N - 1
            elif nx == N:
                nx = 0

            if ny == -1:
                ny = M - 1
            elif ny == M:
                ny = 0

            if donut[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

res = 0
for i in range(N):
    for j in range(M):
        if donut[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            res += 1

print(res)