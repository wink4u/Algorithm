import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

miro = []
flag = 1
sx, sy = 0, 0
for i in range(N):
    temp = list(input().strip())
    miro.append(temp)
    if flag:
        for j in range(len(temp)):
            if temp[j] == '0':
                sx, sy = i, j
                flag = 0
                temp[j] = '.'
                break

visit = [[[False] * (1 << 6) for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((sx, sy, 0, 0))
    visit[sx][sy][0] = True

    while q:
        x, y, cnt, key = q.popleft()

        if miro[x][y] == '1':
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny][key]:
                    if miro[nx][ny] == '1' or miro[nx][ny] == '.':
                        visit[nx][ny][key] = True
                        q.append((nx, ny, cnt + 1, key))
                    elif 'a' <= miro[nx][ny] <= 'f':
                        new_key = key | (1 << (ord(miro[nx][ny]) - ord('a')))
                        visit[nx][ny][new_key] = True
                        q.append((nx, ny, cnt + 1, new_key))
                    elif 'A' <= miro[nx][ny] <= 'Z':
                        value = key & (1 << (ord(miro[nx][ny]) - ord('A')))
                        if value:
                            visit[nx][ny][key] = True
                            q.append((nx, ny, cnt + 1, key))

    return -1

print(bfs())