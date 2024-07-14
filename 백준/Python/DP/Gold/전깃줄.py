import sys
input = sys.stdin.readline

N = int(input())

elec = [list(map(int, input().split())) for _ in range(N)]
elec.sort()

DP = [1] * N
for i in range(1, N):
    for j in range(i):
        if elec[j][1] < elec[i][1]:
            DP[i] = max(DP[i], DP[j] + 1)

print(N - max(DP))