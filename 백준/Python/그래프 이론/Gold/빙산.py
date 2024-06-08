import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def melt(sx, sy, visited):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if ice[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    if d <= 3:
                        if ice[x][y]:
                            ice[x][y] -= 1

    return visited

res = 0
while True:
    res += 1
    visit = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if ice[i][j] and not visit[i][j]:
                visit = melt(i, j, visit)
                cnt += 1

    if cnt == 0:
        print(cnt)
        break
    elif cnt >= 2:
        print(res - 1)
        break
