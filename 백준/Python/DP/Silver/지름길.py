import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [i for i in range(m + 1)]
check = []

for _ in range(n):
    check.append(list(map(int, input().split())))

check.sort()

for st, end, value in check:
    for i in range(1, m + 1):
        if i == end:
            dp[i] = min(dp[i], dp[st] + value)
        else:
            dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[-1])