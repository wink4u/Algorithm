import sys
input = sys.stdin.readline

# n가지 종류의 동전, 가치의 합 k원

n, k = map(int, input().split())

DP = [0] * (k + 1)

for i in range(n):
    DP[i] = 1

# for i in range(1, k + 1):
