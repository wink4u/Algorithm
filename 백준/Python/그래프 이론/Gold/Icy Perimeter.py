import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())

board = [['.'] * (n + 2)]

for _ in range(n):
    tmp = list(input().strip())
    board.append(['.'] + tmp + ['.'])

board.append(['.'] * (n + 2))

check = defaultdict(list)
visit = [[0] * (n + 2) for _ in range(n + 2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
_max = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j] == '#' and not visit[i][j]:
            q = deque()
            q.append((i, j))
            visit[i][j] = 1
            cnt = 1
            dcnt = 0

            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n + 2 and 0 <= ny < n + 2 and not visit[nx][ny]:
                        if board[nx][ny] == '#':
                            cnt += 1
                            visit[nx][ny] = 1
                            q.append((nx, ny))
                        else:
                            dcnt += 1

            _max = max(cnt, _max)
            check[cnt].append(dcnt)

print(_max, min(check[_max]))