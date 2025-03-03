import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

trees = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, v = map(int, input().split())
    trees[r - 1][c - 1].append(v)

arr = [[5] * n for _ in range(n)]

for _ in range(k):

    check = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if len(trees[x][y]):
                trees[x][y].sort()
                idx = -1

                for t in range(len(trees[x][y])):
                    if trees[x][y][t] <= arr[x][y]:
                        arr[x][y] -= trees[x][y][t]
                        trees[x][y][t] += 1

                        if trees[x][y][t] % 5 == 0:
                            check[x][y] += 1

                    else:
                        idx = t
                        break

                if idx != -1:
                    for d in trees[x][y][idx:]:
                        arr[x][y] += d // 2
                    trees[x][y] = trees[x][y][:idx]

    for x in range(n):
        for y in range(n):
            if check[x][y]:
                for c in range(check[x][y]):
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < n and 0 <= ny < n:
                            trees[nx][ny].append(1)

            arr[x][y] += ground[x][y]

res = 0
for i in range(n):
    for j in range(n):
        res += len(trees[i][j])

print(res)