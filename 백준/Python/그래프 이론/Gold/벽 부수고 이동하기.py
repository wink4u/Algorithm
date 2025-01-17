import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sx, sy = 0, 0
ex, ey = n - 1, m - 1

q = deque()
q.append([0, 0, 0, 1])
visit[0][0][0] = 1

while q:
    x, y, flag, cnt = q.popleft()

    if x == ex and y == ey:
        print(cnt)
        exit()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == '0' and not visit[nx][ny][flag]:
                visit[nx][ny][flag] = 1
                q.append([nx, ny, flag, cnt + 1])
            elif board[nx][ny] == '1' and flag == 0:
                if not visit[nx][ny][1]:
                    visit[nx][ny][1] = 1
                    q.append([nx, ny, 1, cnt + 1])

print(-1)