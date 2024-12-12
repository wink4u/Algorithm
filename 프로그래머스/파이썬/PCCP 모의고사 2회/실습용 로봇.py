def solution(command):
    x, y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    d = 0

    for c in command:
        if c == 'G':
            x += dx[d]
            y += dy[d]
        elif c == 'B':
            x -= dx[d]
            y -= dy[d]
        elif c == 'R':
            d += 1
            if d == 4:
                d = 0
        else:
            d -= 1
            if d == -1:
                d = 3

    return [x, y]