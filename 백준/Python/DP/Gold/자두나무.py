import sys

input = sys.stdin.readline

T, W = map(int, input().split())

# 자두에 떨어지는 나무의 번호 1, 2
# 움직일때 안움직일때 기준을 나누어서 값을 구해야할 것 같음

tree = [0]
for _ in range(T):
    tree.append(int(input()))

DP = [[0] * (W + 1) for _ in range(T + 1)]

for i in range(T + 1):

    if tree[i] == 1:
        DP[i][0] = DP[i - 1][0] + 1
    else:
        DP[i][0] = DP[i - 1][0]

    for j in range(1, W + 1):

        if tree[i] == 1 and j % 2 == 0:
            DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + 1
        elif tree[i] == 2 and j % 2 == 1:
            DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + 1
        else:
            DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j])


print(max(DP[T]))

