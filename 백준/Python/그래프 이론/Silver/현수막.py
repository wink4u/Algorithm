import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visit[sx][sy] = 1

    while q:
        x, y = q.popleft()

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny]:
                    if board[nx][ny]:
                        q.append((nx ,ny))
                        visit[nx][ny] = 1

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] and not visit[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)