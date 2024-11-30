import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [-3, -3, -2, -2, 2, 2, 3, 3], [-2, 2, -3, 3, -3, 3, -2, 2]
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

visit = [[0] * 9 for _ in range(10)]
visit[sx][sy] = 0

def can_move(x, y, d):
    tx = [
        [-1, -2],
        [-1, -2],
        [0, -1],
        [0, -1],
        [0, 1],
        [0, 1],
        [1, 2],
        [1, 2]
    ]
    ty = [
        [0, -1],
        [0, 1],
        [-1, -2],
        [1, 2],
        [-1, -2],
        [1, 2],
        [0, -1],
        [0, 1]
    ]

    for i in range(2):
        n_x = x + tx[d][i]
        n_y = y + ty[d][i]
        if (n_x, n_y) == (ex, ey):
            return 0

    return 1

def check():
    q = deque()
    q.append((sx, sy, 0))

    while q:
        x, y, cnt = q.popleft()

        if x == ex and y == ey:
            return cnt

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 10 and 0 <= ny < 9 and not visit[nx][ny]:
                if not can_move(x, y, d):
                    continue

                q.append((nx, ny, cnt + 1))
                visit[nx][ny] = 1
    return -1


print(check())