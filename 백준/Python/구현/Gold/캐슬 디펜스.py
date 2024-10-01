import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

n, m, d = map(int, input().split())

delete = []

board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def attack_bfs(sx, sy, stage, end):
    q = deque()
    q.append((sx, sy))
    visit = [[0] * m for _ in range(len(stage))]

    attack = []
    cnt = 0

    while q:
        for _ in range(len(q)):
            s_x, s_y = q.popleft()

            for d in range(4):
                nx = s_x + dx[d]
                ny = s_y + dy[d]

                if 0 <= nx < len(stage) and 0 <= ny < m and not visit[nx][ny]:
                    if stage[nx][ny]:
                        attack.append([nx, ny])
                    else:
                        q.append((nx, ny))
                    visit[nx][ny] = 1

        if attack:
            break

        cnt += 1

        if cnt == end:
            break

    if attack:
        attack.sort(key = lambda x : x[1])
        return attack[0]
    else:
        return [-1, -1]


def stage_clear(stage):
    if len(stage):
        stage.pop()


combi = list(combinations([i for i in range(m)], 3))
result = []

for i in range(len(combi)):
    game = copy.deepcopy(board)
    count = 0

    while True:
        check = set()

        for j in range(3):
            x, y = len(game), combi[i][j]

            rx, ry = attack_bfs(x, y, game, d)

            if rx != -1 and ry != -1:
                check.add((rx, ry))


        check = list(check)

        for j in range(len(check)):
            game[check[j][0]][check[j][1]] = 0
            count += 1

        stage_clear(game)

        if len(game) == 0:
            result.append(count)
            break

print(max(result))
