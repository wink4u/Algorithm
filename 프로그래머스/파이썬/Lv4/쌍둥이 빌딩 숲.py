def solution(n, count):
    mod = 1000000007
    dp = [[0] * (count + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for k in range(1, n + 1):
        for c in range(1, count + 1):
            dp[k][c] = (dp[k - 1][c - 1] + dp[k - 1][c] * 2 * (k - 1)) % mod

    return dp[n][count]