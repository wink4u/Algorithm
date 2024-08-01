import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))
res = 1e10

L, R = 0, 0
_sum = 0

while L <= R:
    if R == N:
        if _sum < S:
            break
        else:
            res = min(res, R - L)
            _sum -= arr[L]
            L += 1
    else:
        if _sum < S:
            _sum += arr[R]
            R += 1
        else:
            res = min(res, R - L)
            _sum -= arr[L]
            L += 1

if res == 1e10:
    print(0)
else:
    print(res)