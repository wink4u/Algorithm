import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())

# 0 흰색 1 빨간색 2 파란색
board = [list(map(int, input().split())) for _ in range(n)]
check = [[[] for _ in range(n)] for _ in range(n)]
change = {0 : 1, 1: 0, 2: 3, 3: 2}

stone = defaultdict(int)
locate = defaultdict(list)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for num in range(1, k + 1):
    # dir 1 2 3 4 우 좌 상 하
    x, y, dr = map(int, input().split())
    stone[num] = dr - 1
    locate[num] = [x - 1, y - 1]
    check[x - 1][y - 1].append(num)


def move(x, y):
    return 0 <= x < n and 0 <= y < n


turn = 1
flag = 0
while True:
    flag = 0

    for i in range(1, k + 1):
        x, y = locate[i]
        d = stone[i]
        idx = check[x][y].index(i)
        nx, ny = x + dx[d], y + dy[d]
        tmp = check[x][y][idx:]
        l_tmp = len(tmp)

        if not move(nx, ny) or board[nx][ny] == 2:
            d = change[d]
            stone[i] = d
            nx, ny = x + dx[d], y + dy[d]

            if not move(nx, ny) or board[nx][ny] == 2:
                continue

            if board[nx][ny] == 1:
                tmp.reverse()

            for j in range(l_tmp):
                locate[tmp[j]] = [nx, ny]
                check[nx][ny].append(tmp[j])

            check[x][y] = check[x][y][:idx]

        elif board[nx][ny] == 0:
            for j in range(l_tmp):
                locate[tmp[j]] = [nx, ny]
                check[nx][ny].append(tmp[j])

            check[x][y] = check[x][y][:idx]

        elif board[nx][ny] == 1:
            tmp.reverse()
            for j in range(l_tmp):
                locate[tmp[j]] = [nx, ny]
                check[nx][ny].append(tmp[j])

            check[x][y] = check[x][y][:idx]

        if len(check[nx][ny]) >= 4:
            flag = 1
            break

    if flag:
        break

    turn += 1

    if turn > 1000:
        break

if flag:
    print(turn)
else:
    print(-1)

