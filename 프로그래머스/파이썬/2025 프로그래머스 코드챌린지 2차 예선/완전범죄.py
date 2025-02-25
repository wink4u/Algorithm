def solution(info, n, m):
    answer = 1e7
    DP = [[1e7] * (m) for _ in range(len(info) + 1)]
    DP[0][0] = 0

    for i in range(1, len(info) + 1):
        a, b = info[i - 1]
        for j in range(m):
            DP[i][j] = min(DP[i][j], DP[i - 1][j] + a)

            if j + b < m:
                DP[i][j + b] = min(DP[i][j + b], DP[i - 1][j])

    for j in range(m):
        answer = min(DP[len(info)][j], answer)

    return -1 if answer >= n else answer