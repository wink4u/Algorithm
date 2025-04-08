import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

k = 1
while n >= k * k:
    dp[k * k] = 1
    k += 1

for i in range(1, n + 1):
    if dp[i]:
        continue

    j = 1
    while j * j <= i:
        if dp[i] == 0:
            dp[i] = dp[j * j] + dp[i - j * j]
        else:
            dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])

        j += 1

print(dp[n])
