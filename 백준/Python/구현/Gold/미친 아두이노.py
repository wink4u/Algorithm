import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
command = input().strip()

aduino = []
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            x, y = i, j
        elif board[i][j] == 'R':
            aduino.append((i, j))

dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
move = 0

for i in range(len(command)):
    d = int(command[i]) - 1
    x = x + dx[d]
    y = y + dy[d]
    check = set()
    tmp = set()
    move += 1

    if (x, y) in aduino:
        print(f'kraj {move}')
        exit()

    for j in range(len(aduino)):
        rx, ry = aduino[j]
        _min = 100000
        v = 0
        for n_d in range(len(dx)):
            if abs(x - (rx + dx[n_d])) + abs(y - (ry + dy[n_d])) < _min:
                _min = abs(x - (rx + dx[n_d])) + abs(y - (ry + dy[n_d]))
                v = n_d

        rx = rx + dx[v]
        ry = ry + dy[v]

        if rx == x and ry == y:
            print(f'kraj {move}')
            exit()

        if (rx, ry) not in check:
            check.add((rx, ry))
        else:
            tmp.add((rx, ry))

    tmp = list(tmp)
    while tmp:
        tx, ty = tmp.pop()
        check.remove((tx, ty))

    aduino = list(check)


for i in range(n):
    for j in range(m):
        if i == x and j == y:
            board[i][j] = 'I'
        else:
            if (i, j) in aduino:
                board[i][j] = 'R'
            else:
                board[i][j] = '.'

for i in range(n):
    print(''.join(board[i]))