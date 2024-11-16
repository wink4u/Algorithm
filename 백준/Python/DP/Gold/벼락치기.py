import sys
input = sys.stdin.readline

n, t = map(int, input().split())

time = []
score = []

for _ in range(n):
    k, s = map(int, input().split())
    time.append(k)
    score.append(s)

DP = [0] * (t + 1)

for i in range(n):
    for j in range(t, time[i] - 1, -1):
        DP[j] = max(DP[j], DP[j - time[i]] + score[i])

print(DP[-1])