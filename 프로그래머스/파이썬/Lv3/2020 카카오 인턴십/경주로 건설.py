from collections import deque


def solution(board):
    n = len(board)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def bfs(sx, sy, dr, c):
        q = deque()
        q.append([sx, sy, dr, c])
        visit = [[1e8] * n for _ in range(n)]
        visit[sx][sy] = 0

        while q:
            x, y, d, cost = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                    if i == d:
                        ncost = cost + 100
                    else:
                        ncost = cost + 600

                    if ncost < visit[nx][ny]:
                        visit[nx][ny] = ncost
                        q.append([nx, ny, i, ncost])

        return visit[-1][-1]

    return min([bfs(0, 0, 0, 0), bfs(0, 0, 1, 0)])