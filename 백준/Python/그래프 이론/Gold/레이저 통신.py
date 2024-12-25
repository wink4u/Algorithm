import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
se = []
board = []
inf = 1e9
for i in range(n):
    tmp = list(input().strip())
    for j in range(m):
        if tmp[j] == 'C':
            se.append((i, j))
    board.append(tmp)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

sx, sy = se[0]
ex, ey = se[1]

def bfs():
    visit = [[[inf] * 4 for _ in range(m)] for _ in range(n)]
    visit[sx][sy] = [0, 0, 0, 0]

    q = deque()

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "*":
            q.append((nx, ny, i))
            visit[nx][ny][i] = 0

    while q:
        x, y, prev = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != '*':
                cnt = visit[x][y][prev]
                if prev % 2:
                    if d % 2 == 0:
                        cnt += 1
                else:
                    if d % 2:
                        cnt += 1

                if visit[nx][ny][d] == -1:
                    visit[nx][ny][d] = cnt
                    q.append((nx, ny, d))
                else:
                    if visit[nx][ny][d] > cnt:
                        visit[nx][ny][d] = cnt
                        q.append((nx, ny, d))

    return min(visit[ex][ey])

print(bfs())