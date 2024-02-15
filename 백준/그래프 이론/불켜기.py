import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())

visit = [[0 for _ in range(N)] for _ in range(N)]
light = [[0 for _ in range(N)] for _ in range(N)]

sx, sy = 0, 0

room = defaultdict(list)
for i in range(M):
    x, y, a, b = map(int, input().split())
    room[(x - 1, y - 1)].append([a - 1, b - 1])


def bfs():
    cnt = 1
    light[sx][sy] = 1
    visit[sx][sy] = 1
    q = deque()
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        for lx, ly in room[(x, y)]:
            if not light[lx][ly]:
                light[lx][ly] = 1
                cnt += 1

                for d in range(4):
                    lnx = lx + dx[d]
                    lny = ly + dy[d]
                    if 0 <= lnx < N and 0 <= lny < N and visit[lnx][lny]:
                        q.append((lnx, lny))

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and light[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny))

    return cnt

print(bfs())