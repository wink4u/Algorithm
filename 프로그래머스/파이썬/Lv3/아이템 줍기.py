from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    board = [[-1 for _ in range(102)] for _ in range(102)]

    for i in range(len(rectangle)):
        x1, y1, x2, y2 = map(lambda x: x * 2, rectangle[i])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    board[x][y] = 0
                elif board[x][y] != 0:
                    board[x][y] = 1

    q = deque()
    q.append([characterX * 2, characterY * 2])
    visit = [[1 for _ in range(102)] for _ in range(102)]
    visit[characterX * 2][characterY * 2] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        if x == itemX * 2 and y == itemY * 2:
            answer = visit[x][y] // 2
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 102 and 0 <= ny < 102:
                if board[nx][ny] == 1 and visit[nx][ny] == 1:
                    q.append([nx, ny])
                    visit[nx][ny] = visit[x][y] + 1
    return answer