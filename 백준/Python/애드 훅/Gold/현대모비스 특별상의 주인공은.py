import sys
input = sys.stdin.readline

n, m = map(int, input().split())

name = [list(input().split()) for _ in range(n)]
check = set()
ans = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(n):
    for y in range(m):
        if name[x][y] not in check:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < m and name[x][y] == name[nx][ny]:
                    check.add(name[x][y])
                    break
if n >= 3:
    for x in range(n - 2):
        for y in range(m):
            if name[x][y] not in check:
                if name[x][y] == name[x + 2][y]:
                    check.add(name[x][y])

if m >= 3:
    for x in range(n):
        for y in range(m - 2):
            if name[x][y] not in check:
                if name[x][y] == name[x][y + 2]:
                    check.add(name[x][y])

check = list(check)
check.sort()

if check:
    for c in check:
        print(c)
else:
    print('MANIPULATED')