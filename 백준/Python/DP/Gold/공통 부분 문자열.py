import sys
from collections import defaultdict
input = sys.stdin.readline

a = input().strip()
b = input().strip()

R, C = len(a) + 1, len(b) + 1

DP = [[0] * C for _ in range(R)]
_max = 0

for i in range(1, R):
    for j in range(1, C):
        if a[i - 1] == b[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1

    _max = max(_max, max(DP[i]))

print(_max)