import sys
input = sys.stdin.readline

n = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(n, i, -1):
        dp[j] = min(dp[j], dp[i] + dp[j - i])

print(dp[-1])