import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().split()) for _ in range(n)]
teacher = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':
            teacher.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 직선 방향으로 확인
        while 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 'O':
            if board[nx][ny] == 'S':
                return False
            else:
                nx += dx[d]
                ny += dy[d]
    return True

result = False

def combination(cnt):
    global result
    if cnt == 3:
        for x, y in teacher:
            if not check(x, y):
                return
        result = True
        return

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                cnt += 1
                board[i][j] = 'O'
                combination(cnt)
                board[i][j] = 'X'
                cnt -= 1

combination(0)

if result:
    print('YES')
else:
    print('NO')