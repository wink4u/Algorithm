from collections import deque


def solution(n, m, hole):
    answer = 0
    visit = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    board = [[0] * m for _ in range(n)]

    for a, b in hole:
        board[a - 1][b - 1] = 1

    q = deque()
    q.append((0, 0, False))
    visit[0][0][False] = True

    while q:
        for _ in range(len(q)):
            x, y, ismove = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny][ismove] and board[nx][ny] == 0:
                    if (nx, ny) == (n - 1, m - 1):
                        return answer + 1

                    visit[nx][ny][ismove] = True
                    q.append((nx, ny, ismove))

                if not ismove:
                    nx += dx[d]
                    ny += dy[d]

                    if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny][True] and board[nx][ny] == 0:
                        if (nx, ny) == (n - 1, m - 1):
                            return answer + 1
                        visit[nx][ny][True] = True
                        q.append((nx, ny, True))

        answer += 1

    return -1

