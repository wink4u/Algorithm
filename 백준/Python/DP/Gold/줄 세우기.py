import sys
input = sys.stdin.readline

n = int(input())
dp = [[0, 0] for _ in range(n + 1)]
_max = 0

for i in range(1, n + 1):
    student = int(input())
    for j in range(i):
        if dp[j][0] < student:
            dp[i] = [student, max(dp[j][1] + 1, dp[i][1])]
            _max = max(_max, dp[i][1])

print(n - _max)
