import sys
input = sys.stdin.readline

n = int(input())
dp = [[1e9] * 58 for _ in range(58)]

for _ in range(n):
    p, q = input().strip().split(' => ')
    dp[ord(p) - 65][ord(q) - 65] = 0


for k in range(58):
    for i in range(58):
        for j in range(58):
            if i == j:
                continue
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = []

for i in range(58):
    for j in range(58):
        if i != j and dp[i][j] == 0:
            ans.append(f'{chr(i + 65)} => {chr(j + 65)}')

print(len(ans))
for a in ans:
    print(a)