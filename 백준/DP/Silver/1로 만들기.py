import sys
import math
input = sys.stdin.readline

N = int(input())

DP = [math.pow(10, 6)] * (N + 4)

DP[1] = 0
DP[2] = DP[3] = 1

for i in range(4, N + 4):
    if i % 3 == 0 and i % 2 ==0:
        DP[i] = min(DP[i // 3], DP[i // 2], DP[i - 1]) + 1
    elif i % 3 == 0:
        DP[i] = min(DP[i // 3], DP[i - 1]) + 1
    elif i % 2 == 0:
        DP[i] = min(DP[i // 2], DP[i - 1]) + 1
    else:
        DP[i] = DP[i - 1] + 1

print(DP[N])