import sys
input = sys.stdin.readline

n, k = map(int, input().split())
study = []
for i in range(k):
    study.append(list(map(int, input().split())))

dp = [0] * (n + 1)

for i in range(k):
    v, time = study[i]
    for j in range(n, time - 1, -1):
        dp[j] = max(dp[j], dp[j - time] + v)

print(dp[n])