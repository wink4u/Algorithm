import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

RGB = [list(map(int, input().split())) for _ in range(N)]

T = int(input())

res = 0

arr = [[] for _ in range(N)]

for i in range(len(RGB)):

    for j in range(0, len(RGB[i]), 3):
        total = sum(RGB[i][j:j+3])
        if total / 3 >= T:
            arr[i].append(1)
        else:
            arr[i].append(0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[0 for _ in range(M)] for _ in range(N)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if arr[nx][ny] == 1:
                    visit[nx][ny] = 1
                    q.append((nx, ny))



for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visit[i][j]:
            bfs(i, j)
            res += 1

print(res)

