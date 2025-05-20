import sys
input = sys.stdin.readline

n = int(input())

if n <= 5:
    print(n)
else:
    plus = 1
    flag = 0
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + plus
        if flag == 1:
            plus += 1
            flag = 0

        if i % 6 == 0:
            dp[i] += 1
            flag = 1

    print(dp[-1])