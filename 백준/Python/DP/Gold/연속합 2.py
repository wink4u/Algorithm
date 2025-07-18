import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 0 idx 더한거, 1 idx 안 더한거
dp = [[x for x in arr] for _ in range(2)]

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + arr[i], dp[0][i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])

print(max(max(dp[0]), max(dp[1])))