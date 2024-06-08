import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_sum = [[0 for _ in range(N + 1)]]

for i in range(N):
    num = list(map(int, input().split()))
    total = 0
    tmp = [0]

    for j in range(N):
        total += num[j]
        tmp.append(total)

    _sum.append(tmp)

for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    res = 0
    for i in range(sx, ex + 1):
        res += _sum[i][ey] - _sum[i][sy - 1]

    print(res)