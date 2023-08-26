import sys
input = sys.stdin.readline

# 물품의 수 N, 버틸 수 있는 무게 K
N, K = map(int, input().split())

DP = [0] * (K + 1)
weight = []
value = []

for i in range(N):
    wei, val = map(int, input().split())
    weight.append(wei)
    value.append(val)

for i in range(N):
    for j in range(K, weight[i] - 1, -1):
        DP[j] = max(DP[j], DP[j - weight[i]] + value[i])

print(DP[K])