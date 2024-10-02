import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2 ** n)]
command = list(map(int, input().split()))

ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

edge = [[0, 0], [0, 2 ** n - 1], [2 ** n - 1, 0], [2 ** n - 1, 2 ** n - 1]]

def input_data(arr, num, t, k):
    z_arr = list(map(list, zip(*arr)))

    for i in range(len(z_arr)):
        z_arr[i].reverse()

    for i in range(2 ** num):
        for j in range(2 ** num):
            board[i + t][j + k] = z_arr[i][j]


def trans(num):
    for t in range(0, 2 ** n, 2 ** num):
        for k in range(0, 2 ** n, 2 ** num):
            arr = []
            for cnt in range(2 ** num):
                tmp = board[t + cnt][k: k + 2 ** num]
                arr.append(tmp)

            input_data(arr, num, t, k)


def remove_edge():
    for r in range(4):
        if board[edge[r][0]][edge[r][1]]:
            board[edge[r][0]][edge[r][1]] -= 1

for c in command:
    if c:
        trans(c)
        # remove_edge()

    remove = []

    for x in range(2 ** n):
        for y in range(2 ** n):
            if [x, y] in edge:
                remove.append([x, y])
            else:
                cnt = 0

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                        if board[nx][ny]:
                            cnt += 1

                if cnt < 3:
                    remove.append([x, y])

    if remove:
        for rx, ry in remove:
            if board[rx][ry]:
                board[rx][ry] -= 1

visit = [[0] * 2 ** n for _ in range(2 ** n)]
res = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if not visit[i][j] and board[i][j]:
            count = 1
            visit[i][j] = 1
            q = deque()
            q.append((i, j))

            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n and not visit[nx][ny]:
                        if board[nx][ny]:
                            visit[nx][ny] = 1
                            q.append((nx, ny))
                            count += 1

            res = max(res, count)

_sum = 0
for i in range(len(board)):
    _sum += sum(board[i])

print(_sum)
print(res)
