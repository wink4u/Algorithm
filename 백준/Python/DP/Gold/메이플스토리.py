import sys
input = sys.stdin.readline

n, t = map(int, input().split())
DP = [[-1] * n for _ in range(t + 1)]
arr = []

for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        DP[0][i] = 0

    arr.append((a, b))

move = [list(map(int, input().split())) for _ in range(n)]


for i in range(1, t + 1):
    for j in range(n):
        can, up = arr[j]

        if DP[i - 1][j] >= can:
            DP[i][j] = DP[i - 1][j] + up

        for k in range(n):
            if j != k and i - move[k][j] >= 0 and DP[i - move[k][j]][k] >= can:
                DP[i][j] = max(DP[i][j], DP[i - move[k][j]][k])


print(max(DP[-1]))