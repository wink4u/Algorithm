import sys
input = sys.stdin.readline

arr = list(map(int, input().strip()))
n = len(arr)

if arr[0] == 0:
    print(0)
else:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(1, n):
        k = i + 1
        if arr[i] > 0:
            dp[k] += dp[k - 1]

        tmp = arr[i - 1] * 10 + arr[i]

        if 10 <= tmp <= 26:
            dp[k] += dp[k - 2]

    print(dp[n] % 1000000)