import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

L, R = min(arr), max(arr) * M
res = R

while L <= R:
    total = 0
    mid = (L + R) // 2

    for i in range(N):
        total += mid // arr[i]

    if total >= M:
        R = mid - 1
        res = min(res, mid)
    else:
        L = mid + 1

print(res)