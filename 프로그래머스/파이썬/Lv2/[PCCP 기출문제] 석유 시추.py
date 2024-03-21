from collections import defaultdict, deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

value = defaultdict(int)


def solution(land):
    N, M = len(land), len(land[0])

    visit = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0

    def bfs(sx, sy):
        q = deque()
        q.append((sx, sy))
        visit[sx][sy] = 1
        res = 1
        check = set()
        check.add(sy)

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                    if land[nx][ny]:
                        q.append((nx, ny))
                        visit[nx][ny] = 1
                        res += 1
                        check.add(ny)

        for check_v in check:
            value[check_v] += res

    for i in range(N):
        for j in range(M):
            if land[i][j] and not visit[i][j]:
                bfs(i, j)

    temp = sorted(list(value.items()), key=lambda x: (-x[1], x[0]))

    return temp[0][1]