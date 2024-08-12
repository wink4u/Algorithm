import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
M, N = map(int, input().split())

hx = [-2, -2, -1, -1, 2, 2, 1, 1]
hy = [-1, 1, -2, 2, -1, 1, -2, 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = [list(map(int, input().split())) for _ in range(N)]

sx, sy, ex, ey = 0, 0, N - 1, M - 1

def bfs():
    q = deque()
    q.append([sx, sy, 0])
    visit = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    visit[0][0][0] = 1

    while q:
        x, y, k_cnt = q.popleft()

        if x == ex and y == ey:
            return visit[x][y][k_cnt] - 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and not board[nx][ny]:
                if not visit[nx][ny][k_cnt]:
                    visit[nx][ny][k_cnt] = visit[x][y][k_cnt] + 1
                    q.append([nx, ny, k_cnt])

        if k_cnt < K:
            for d in range(8):
                nx = x + hx[d]
                ny = y + hy[d]

                if 0 <= nx < N and 0 <= ny < M and not board[nx][ny]:
                    if not visit[nx][ny][k_cnt + 1]:
                        visit[nx][ny][k_cnt + 1] = visit[x][y][k_cnt] + 1
                        q.append([nx, ny, k_cnt + 1])

    return -1

print(bfs())