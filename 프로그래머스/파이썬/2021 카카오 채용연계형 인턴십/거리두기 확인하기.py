def solution(places):
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    answer = []

    def check(board):
        for x in range(5):
            for y in range(5):
                if board[x][y] == 'P':
                    for t in range(1, 3):
                        if 0 <= x - t < 5:
                            if board[x - t][y] == 'X':
                                break
                            elif board[x - t][y] == 'P':
                                return 0
                        else:
                            break

                    for t in range(1, 3):
                        if 0 <= y - t < 5:
                            if board[x][y - t] == 'X':
                                break
                            elif board[x][y - t] == 'P':
                                return 0
                        else:
                            break

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if board[nx][ny] == 'P':
                                if d == 0:
                                    if board[nx + 1][ny] != 'X' or board[nx][ny + 1] != 'X':
                                        return 0
                                elif d == 1:
                                    if board[nx + 1][ny] != 'X' or board[nx][ny - 1] != 'X':
                                        return 0
                                elif d == 2:
                                    if board[nx - 1][ny] != 'X' or board[nx][ny + 1] != 'X':
                                        return 0
                                else:
                                    if board[nx - 1][ny] != 'X' or board[nx][ny - 1] != 'X':
                                        return 0

        return 1

    for i in range(5):
        answer.append(check(places[i]))

    return answer