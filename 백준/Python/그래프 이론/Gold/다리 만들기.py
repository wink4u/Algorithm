import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

land = 1

check = defaultdict(list)

for i in range(n):
    for j in range(n):
        if board[i][j] and not visit[i][j]:
            q = deque()
            q.append((i, j))
            visit[i][j] = land

            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                        if board[nx][ny]:
                            q.append((nx, ny))
                            visit[nx][ny] = land
                        else:
                            check[land].append((nx, ny))
            land += 1


res = 1e9
check_item = list(check.items())

for i in range(land - 1):
    now, arr = check_item[i]

    for j in range(len(arr)):
        sx, sy = arr[j]
        v = [[0] * n for _ in range(n)]
        v[sx][sy] = 1
        q = deque()
        q.append((sx, sy))
        flag = 0

        while q:
            x, y = q.popleft()

            if flag:
                break

            if visit[x][y] > res:
                break

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < n and not v[nx][ny]:
                    if not board[nx][ny]:
                        q.append((nx, ny))
                        v[nx][ny] = v[x][y] + 1
                    else:
                        if now != visit[nx][ny]:
                            res = min(res, v[x][y])
                            flag = 1

print(res)