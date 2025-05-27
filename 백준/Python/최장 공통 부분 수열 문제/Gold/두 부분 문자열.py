import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

h, w = len(A), len(B)

DP = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if A[i - 1] == B[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

print(len(A) + len(B) - DP[-1][-1])