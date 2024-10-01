import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline

# 아기 상어 초기 크기 2
# 1초당 상하좌우로 인접한 한칸씩 이동
# 큰 물고기가 있는칸 지날 수 없음
# 같은 크기는 지나갈 수 만있음
# 자신의 크기와 같은 수의 물고리를 먹을때마다 크기가 1 증가

n = int(input())
# 아기 상어가 뛰놀 수 있는 리스트 초기 배열
board = []
# sx, sy 아기상어의 초기 x, y power 2 eat 먹은 변수
sx, sy, power, eat = 0, 0, 2, 0

# dx, dy direction
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        sx, sy = i, tmp.index(9)


    board.append(tmp)

board[sx][sy] = 0
def find_bfs(ex, ey):
    global eat, power

    q = deque()
    q.append((ex, ey))
    visit = [[0] * n for _ in range(n)]
    visit[ex][ey] = 1

    eat_list = []

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                if board[nx][ny] == 0 or board[nx][ny] == power:
                    q.append((nx, ny))
                elif board[nx][ny] < power:
                    eat_list.append([nx, ny, visit[nx][ny]])


    if len(eat_list) > 0:
        eat_list.sort(key = lambda x : (x[2], x[0], x[1]))
        rx, ry = eat_list[0][0], eat_list[0][1]

        eat += 1
        if power == eat:
            power += 1
            eat = 0

        board[eat_list[0][0]][eat_list[0][1]] = 0

        return [visit[rx][ry] - 1, rx, ry]
    else:
        return [0]

res = 0

while True:
    bfs_res = find_bfs(sx, sy)
    if bfs_res[0]:
        sx, sy = bfs_res[1], bfs_res[2]
        res += bfs_res[0]
    else:
        break

print(res)