import sys
input = sys.stdin.readline

T, W = map(int, input().split())
DP = [[0 for _ in range(W + 1)] for _ in range(T + 1)]
cnt = 0

for i in range(1, T + 1):
    fruit = int(input())

    if cnt > W:
        cnt = W + 1
    else:
        cnt += 1

    for j in range(cnt):
        if j == 0:
            DP[i][j] = DP[i - 1][j]
        else:
            DP[i][j] += max(DP[i - 1][j], DP[i - 1][j - 1])

    for j in range(W + 1):
        if fruit == 1 and j % 2 == 0:
            DP[i][j] += 1
        elif fruit == 2 and j % 2:
            DP[i][j] += 1

print(max(DP[T]))