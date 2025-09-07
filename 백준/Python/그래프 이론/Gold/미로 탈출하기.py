import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

check = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    if i == 0 or i == n - 1:
        for j in range(m):
            if j == 0 and arr[i][j] == 'L':
                check.append((i, j))
                continue
            if j == m - 1 and arr[i][j] == 'R':
                check.append((i, j))
                continue

            if i == 0:
                if arr[i][j] == 'U':
                    check.append((i, j))
            elif i == n - 1:
                if arr[i][j] == 'D':
                    check.append((i, j))
    else:
        if arr[i][0] == 'L':
            check.append((i, 0))
        if arr[i][m - 1] == 'R':
            check.append((i, m - 1))


visit = [[0] * m for _ in range(n)]
ans = 0

for cx, cy in check:
    if not visit[cx][cy]:
        ans += 1
        visit[cx][cy] = 1
        q = deque()
        q.append((cx, cy))

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                    flag = 0
                    if d == 0 and arr[nx][ny] == 'D':
                        flag = 1
                    elif d == 1 and arr[nx][ny] == 'U':
                        flag = 1
                    elif d == 2 and arr[nx][ny] == 'R':
                        flag = 1
                    elif d == 3 and arr[nx][ny] == 'L':
                        flag = 1

                    if flag:
                        q.append((nx, ny))
                        visit[nx][ny] = 1
                        ans += 1

print(ans)