def solution(board):
    O = []
    X = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                O.append([i, j])
            elif board[i][j] == 'X':
                X.append([i, j])

    def win(x, y, n_board):
        cnt = 0
        for i in range(3):
            if n_board[i][y] == n_board[x][y]:
                cnt += 1

            if cnt == 3:
                return 1

        cnt = 0
        for i in range(3):
            if n_board[x][i] == n_board[x][y]:
                cnt += 1

            if cnt == 3:
                return 1

        if x == y:
            cnt = 0
            for i in range(3):
                if n_board[i][i] == n_board[x][y]:
                    cnt += 1

                if cnt == 3:
                    return 1

            cnt = 0
            if x == 1 and y == 1:
                for i in range(3):
                    if n_board[i][2 - i] == n_board[x][y]:
                        cnt += 1

                    if cnt == 3:
                        return 1

        elif (x == 0 and y == 2) or (x == 2 and y == 0):
            cnt = 0
            if x == 1 and y == 1:
                for i in range(3):
                    if n_board[i][2 - i] == n_board[x][y]:
                        cnt += 1

                    if cnt == 3:
                        return 1

        return 0

    if len(O) < len(X):
        return 0
    elif len(O) > len(X):

        if len(O) - len(X) != 1:
            return 0

        flag = 0
        for x, y in X:
            if win(x, y, board):
                flag = 1
                break

        if flag:
            return 0
        else:
            return 1
    else:
        flag = 0
        for x, y in O:
            if win(x, y, board):
                flag = 1
                break

        if flag:
            return 0
        else:
            return 1

