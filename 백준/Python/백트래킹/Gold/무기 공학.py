import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [[-1, 0], [-1, 0], [1, 0], [1, 0]]
dy = [[0, -1], [0, 1], [0, -1], [0, 1]]
visit = [[0] * m for _ in range(n)]
ans = 0

def dfs(x, y, total):
    global ans
    if y == m:
        x += 1
        y = 0
    if x == n:
        ans = max(ans, total)
        return

    if not visit[x][y]:
        for d in range(4):
            nx1 = x + dx[d][0]
            ny1 = y + dy[d][0]
            nx2 = x + dx[d][1]
            ny2 = y + dy[d][1]

            if 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < m and 0 <= ny2 < m:
                if not visit[nx1][ny1] and not visit[nx2][ny2]:
                    visit[x][y] = 1
                    visit[nx1][ny1] = 1
                    visit[nx2][ny2] = 1
                    tmp = arr[x][y] * 2 + arr[nx1][ny1] + arr[nx2][ny2]
                    dfs(x, y + 1, total + tmp)
                    visit[x][y] = 0
                    visit[nx1][ny1] = 0
                    visit[nx2][ny2] = 0
    dfs(x, y + 1, total)


dfs(0, 0, 0)
print(ans)
