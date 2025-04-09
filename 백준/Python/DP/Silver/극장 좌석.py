import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1

if m:
    prev = 0

    for i in range(m):
        answer *= dp[vip[i] - 1 - prev]
        prev = vip[i]

    answer *= dp[n - prev]
else:
    answer = dp[n]

print(answer)
