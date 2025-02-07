import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stuff = []

for _ in range(n):
    stuff.append(list(map(int, input().split())))

bag = [int(input()) for _ in range(k)]
_max = max(bag)

dp = [0] * (_max + 1)


for w, v in stuff:
    for i in range(_max, w - 1, -1):
        dp[i] = max(dp[i - w] + v, dp[i])

res = []
for i in range(k):
    res.append([i + 1, dp[bag[i]] / bag[i]])

res.sort(key = lambda x : (-x[1], x[0]))
print(res[0][0])