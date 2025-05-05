import sys
input = sys.stdin.readline

n = int(input())

h = list(map(int, input().split()))
j = list(map(int, input().split()))

dp = [0] * 101

for i in range(n):
    v, w = h[i], j[i]

    for k in range(100, v, -1):
        dp[k] = max(dp[k], dp[k - v] + w)

print(dp[-1])