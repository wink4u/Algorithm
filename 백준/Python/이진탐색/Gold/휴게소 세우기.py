import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
highway = [0] + list(map(int, input().split())) + [L]

highway.sort()

start, end = 1, L - 1
res = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for i in range(1, len(highway)):
        if highway[i] - highway[i - 1] > mid:
            cnt += (highway[i] - highway[i - 1] - 1) // mid

    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)