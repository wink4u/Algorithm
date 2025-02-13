import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []

sx, sy = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[-1] * m for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 0:
            visit[i][j] = 0
        elif tmp[j] == 2:
            sx, sy = i, j
    board.append(tmp)


q = deque()
q.append((sx, sy))
visit[sx][sy] = 0

while q:
    x, y = q.popleft()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == -1:
            if board[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))


for i in range(n):
    print(*visit[i])