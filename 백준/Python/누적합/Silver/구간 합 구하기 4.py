import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

_sum = [0]

for i in range(N):
    _sum.append(num[i] + _sum[i])

for _ in range(M):
    i, j = map(int, input().split())
    print(_sum[j] - _sum[i - 1])