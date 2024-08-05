import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
res = 0

x, y = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0])
    visit = [[0] * M for _ in range(N)]
    one = []
    check = set()
    visit[0][0] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if board[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                elif board[nx][ny] == 1:
                    if [nx, ny] in one:
                        check.add((nx, ny))
                    else:
                        one.append([nx, ny])

    check_list = list(check)
    for x, y in check_list:
        board[x][y] = 0

    for i in range(N):
        tmp = sum(board[i])
        if tmp:
            return False

    return True

while True:
    if bfs():
        res += 1
        print(res)
        break
    else:
        res += 1