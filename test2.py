import sys
input = sys.stdin.readline

m, n = map(int, input().split())
cookies = list(map(int, input().split()))

start, end = 1, int(1e9)

res = 0

while start <= end:
    mid = (start + end) // 2

    make = 0
    for cookie in cookies:
        make += cookie // mid

    if make >= m:
        res = max(res, mid)
        start = mid + 1
    else:
        end = mid - 1

print(res)