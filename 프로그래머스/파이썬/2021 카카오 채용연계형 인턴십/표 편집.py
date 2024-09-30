def solution(n, k, cmd):
    board = {i: [i - 1, i + 1] for i in range(n)}
    table = ['O'] * n
    delete = []

    for c in cmd:
        c = c.split()

        if c[0] == 'D':
            for _ in range(int(c[1])):
                k = board[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[1])):
                k = board[k][0]
        elif c[0] == 'C':
            prev, nxt = board[k]
            table[k] = 'X'
            delete.append((prev, k, nxt))

            if nxt == n:
                k = board[k][0]
            else:
                k = board[k][1]

            if prev == -1:
                board[nxt][0] = prev
            elif nxt == n:
                board[prev][1] = nxt
            else:
                board[prev][1] = nxt
                board[nxt][0] = prev
        else:
            prev, now, nxt = delete.pop()
            table[now] = 'O'

            if prev == -1:
                board[nxt][0] = now
            elif nxt == n:
                board[prev][1] = now
            else:
                board[prev][1] = now
                board[nxt][0] = now

    return ''.join(table)