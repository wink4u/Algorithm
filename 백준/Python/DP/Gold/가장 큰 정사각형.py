import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if board[i][j]:
            if i >= 1 and j >= 1:
                if board[i - 1][j] and board[i][j - 1] and board[i - 1][j - 1]:
                    board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
                    answer = max(answer, board[i][j])
            else:
                answer = max(answer, 1)

print(answer ** 2)