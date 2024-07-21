import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 동 서 남 북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

command = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

def roll(c):
    if c == 1:
        d = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    elif c == 2:
        d = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif c == 3:
        d = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    else:
        d = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]

    return d

for i in range(K):
    nx, ny = x + dx[command[i] - 1], y + dy[command[i] - 1]

    if 0 <= nx < N and 0 <= ny < M:
        num = board[nx][ny]
        dice = roll(command[i])
        print(dice[0])

        if num:
            dice[5] = num
            board[nx][ny] = 0
        else:
            board[nx][ny] = dice[5]

        x, y = nx, ny
