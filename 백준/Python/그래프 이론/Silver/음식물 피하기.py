import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [['.' for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = '#'

res = 0
visit = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if board[i][j] == '#' and not visit[i][j]:
            visit[i][j] = 1
            q = deque()
            q.append((i, j))
            cnt = 1
            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '#':
                        if not visit[nx][ny]:
                            visit[nx][ny] = 1
                            cnt += 1
                            q.append((nx, ny))

            res = max(res, cnt)

print(res)

