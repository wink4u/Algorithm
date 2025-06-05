import sys
input = sys.stdin.readline

n, m, a, b = map(int, input().split())
item = [[1, 1]]

for _ in range(a):
    x, y = map(int, input().split())
    item.append([x, y])

item.append([n, m])

dp = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(b):
    x, y = map(int, input().split())
    dp[x][y] = -1

item.sort(key = lambda x : (x[0], x[1]))

dp[1][1] = 1

for i in range(1, len(item)):
    sx, sy = item[i - 1]
    ex, ey = item[i]

    for x in range(sx, ex + 1):
        for y in range(sy, ey + 1):
            if dp[x][y] != -1 and not (x == sx and y == sy):
                left = dp[x][y - 1]
                down = dp[x - 1][y]

                if left != -1 and down != -1:
                    dp[x][y] = left + down
                elif left == -1:
                    dp[x][y] = down
                else:
                    dp[x][y] = left


print(dp[n][m])