import sys
input = sys.stdin.readline

n, k = map(int, input().split())
C = [int(input()) for _ in range(n)]
DP = [0 for i in range(k + 1)]
DP[0] = 1

for i in C:
    for j in range(i, k + 1):
        if j - i >= 0:
            DP[j] += DP[j - i]

print(DP[k])