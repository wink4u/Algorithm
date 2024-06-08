import sys
input = sys.stdin.readline
from collections import deque

keybords = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l','.'],['z','x','c','v','b','n','m','.','.','.']]

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy, obj):
    q = deque()
    q.append((sx, sy))
    visit = [[-1 for _ in range(10)] for _ in range(3)]
    visit[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 3 and 0 <= ny < 10 and keybords[nx][ny] != '.':
                if visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1

                    if keybords[nx][ny] == obj:
                        return visit[nx][ny]

                    q.append((nx, ny))


    return 0

for _ in range(T):
    words, m = input().split()

    base = []
    for word in words:
        for i in range(3):
            if word in keybords[i]:
                _index = keybords[i].index(word)
                base.append((i, _index))

    result = []
    for _ in range(int(m)):
        new_words = input().strip()
        cnt = 0

        for i in range(len(new_words)):
            if new_words[i] == words[i]:
                continue

            cnt += bfs(base[i][0], base[i][1], new_words[i])

        result.append([new_words, cnt])

    result.sort(key = lambda x : (x[1], x[0]))

    for i in range(int(m)):
        print(*result[i])


