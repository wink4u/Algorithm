import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
ladder = dict()
snake = dict()

board = [0] * 101
visit = [0] * 101

for i in range(N):
    a, b = map(int, input().split())
    ladder[a] = b

for i in range(M):
    a, b = map(int, input().split())
    snake[a] = b


q = deque([1])

while q:
    now = q.popleft()

    if now == 100:
        print(board[now])
        break

    for dice in range(1, 7):
        next = now + dice

        if next <= 100 and not visit[next]:
            if next in ladder.keys():
                next = ladder[next]

            if next in snake.keys():
                next = snake[next]

            if not visit[next]:
                visit[next] = 1
                board[next] = board[now] + 1
                q.append(next)