import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

res = 0
def check(x, y, move):
    global res
    if x == N - 1 and y == N - 1:
        res += 1
        return

    if x + 1 < N and y + 1 < N:
        if house[x + 1][y + 1] == 0 and house[x][y + 1] == 0 and house[x + 1][y] == 0:
            check(x + 1, y + 1, 2)

    if move == 0 or move == 2:
        if y + 1 < N:
            if house[x][y + 1] == 0:
                check(x, y + 1, 0)

    if move == 1 or move == 2:
        if x + 1 < N :
            if house[x + 1][y] == 0:
                check(x + 1, y, 1)


check(0, 1, 0)
print(res)


