import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_sum = []

for i in range(N):
    total = 0
    num = list(map(int, input().split()))
    arr = [total]
    for j in range(M):
        total += num[j]
        arr.append(total)

    _sum.append(arr)

K = int(input())

for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    res = 0
    for i in range(sx - 1, ex):
        res += _sum[i][ey] - _sum[i][sy - 1]
    print(res)