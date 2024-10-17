import sys
from collections import deque, defaultdict
input = sys.stdin.readline

m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

res = defaultdict(int)

ans1 = 0
ans2 = 0

def bfs(sx, sy, c):
    global ans1

    q = deque()
    q.append([sx, sy])
    visit[sx][sy] = c
    cnt = 1
    while q:
        x, y = q.popleft()
        arr = []

        for d in range(3, -1, -1):
            num = 1 << d

            if board[x][y] >= num:
                board[x][y] -= num
                arr.append(num)

        for d in range(3, -1, -1):
            num = 1 << d

            if num not in arr:
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                    visit[nx][ny] = c
                    q.append([nx, ny])
                    cnt += 1

    res[c] = cnt
    ans1 = max(cnt, ans1)

check = 1

for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            bfs(i, j, check)
            check += 1

def bfs2():
    global ans2
    q = deque()
    q.append((0, 0))
    v = [[0 for _ in range(m)] for _ in range(n)]
    v[0][0] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
                if visit[x][y] != visit[nx][ny]:
                    a, b = visit[x][y], visit[nx][ny]
                    ans2 = max(ans2, res[a] + res[b])

                v[nx][ny] = 1
                q.append([nx, ny])

bfs2()

print(check - 1)
print(ans1)
print(ans2)