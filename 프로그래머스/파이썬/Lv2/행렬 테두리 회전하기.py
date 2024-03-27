def solution(rows, columns, queries):
    answer = []

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    board = [[j + 1 + columns * i for j in range(columns)] for i in range(rows)]

    for i in range(len(queries)):
        x1, y1, x2, y2 = queries[i]
        _min = board[x1 - 1][y1 - 1]
        tmp = _min
        x, y = x1 - 1, y1 - 1

        d = 0
        while True:
            nx = x + dx[d]
            ny = y + dy[d]

            if x1 - 1 <= nx < x2 and y1 - 1 <= ny < y2:
                _min = min(_min, board[nx][ny])

                temp = board[nx][ny]
                board[nx][ny] = tmp
                tmp = temp

                if nx == x1 - 1 and ny == y1 - 1:
                    break
                x = nx
                y = ny
            else:
                d += 1
                if d == 4:
                    d = 0

        answer.append(_min)

    return answer