import sys
input = sys.stdin.readline

n, k = map(int, input().split())

DP = [100001] * (k + 1)

# 단일 동전으로 꾸릴 수 있는가
# 없다면 다른동전을 통해 만들 수 있는가

coin = [int(input()) for _ in range(n)]
DP[0] = 0

for i in range(n):
    c = coin[i]

    for j in range(c, k + 1):
        DP[j] = min(DP[j], DP[j - c] + 1)

if DP[k] == 100001:
    print(-1)
else:
    print(DP[k])
