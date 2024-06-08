import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
count = 0
cheese = []

for i in range(N):
    tmp = list(map(int, input().split()))
    count += tmp.count(1)
    cheese.append(tmp)

sx, sy = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    global count
    q = deque()
    q.append((sx, sy))
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[sx][sy] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if cheese[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = 1
                else:
                    visit[nx][ny] = 2
                    count -= 1

    for i in range(N):
        for j in range(M):
            if visit[i][j] == 2:
                cheese[i][j] -= 1

    if count:
        return True
    else:
        return False

year = 1
while True:
    tmp = count
    res = check()
    if res:
        year += 1
    else:
        print(year)
        print(tmp)
        break


