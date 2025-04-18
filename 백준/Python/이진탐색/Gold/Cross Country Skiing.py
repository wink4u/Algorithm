import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
point = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j]:
            point.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(D):
    q = deque()
    px, py = point[0]

    q.append((px, py))
    visit = [[0] * m for _ in range(n)]
    visit[px][py] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if abs(arr[x][y] - arr[nx][ny]) <= D:
                    visit[nx][ny] = 1
                    q.append((nx, ny))

    for c in range(len(point)):
        cx, cy = point[c]
        if not visit[cx][cy]:
            return False

    return True


if n == 1:
    print(0)
else:
    res = 1e9
    left, right = 0, 1e9
    while left <= right:
        mid = int((left + right) // 2)
        if check(mid):
            res = min(res, mid)
            right = mid - 1
        else:
            left = mid + 1

    print(res)