from collections import deque


def solution(maps):
    answer = 0

    N, M = len(maps), len(maps[0])
    sx, sy = 0, 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        if "S" in maps[i]:
            sx, sy = i, maps[i].index("S")
            break

    def escape(ex, ey, value):
        visit = [[0 for _ in range(M)] for _ in range(N)]
        visit[ex][ey] = value
        q = deque()
        q.append((ex, ey))

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                    if maps[nx][ny] != 'X':
                        if maps[nx][ny] == 'E':
                            return visit[x][y] + 1
                        else:
                            visit[nx][ny] = visit[x][y] + 1
                            q.append((nx, ny))
        return -1

    def check():
        visit = [[0 for _ in range(M)] for _ in range(N)]
        visit[sx][sy] = 1
        q = deque()
        q.append((sx, sy))

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                    if maps[nx][ny] != 'X':
                        if maps[nx][ny] == 'L':
                            return escape(nx, ny, visit[x][y] + 1)
                        else:
                            visit[nx][ny] = visit[x][y] + 1
                            q.append((nx, ny))

        return -1

    res = check()

    if res == -1:
        return -1
    else:
        return res - 1