import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    visit = [[0] * n for _ in range(n)]
    visit[sx][sy] = 1

    q = deque()
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        if x == ex and y == ey:
            print(visit[x][y] - 1)
            break

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
