import sys
input = sys.stdin.readline

N = int(input())

DP = [0 for _ in range(91)]

DP[1] = 1
DP[2] = 1
DP[3] = 2
if N >= 4:
    for i in range(4, N + 1):
        for j in range(1, i-1):
            DP[i] += DP[j]

        DP[i] += 1
print(DP[N])