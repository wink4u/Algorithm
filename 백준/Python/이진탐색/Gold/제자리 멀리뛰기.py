import sys
input = sys.stdin.readline

d, n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

left = 0
right = d

def check(num):
    cnt = 0
    dist = d
    now = 0
    for a in arr:
        if a - now >= num:
            dist = min(dist, a - now)
            now = a
        else:
            cnt += 1

    dist = min(dist, d - now)

    if cnt > m:
        return [True, 0]
    else:
        return [False, dist]


res = 0
while left <= right:
    mid = (left + right) // 2

    bb, dd = check(mid)

    if bb:
        right = mid - 1
    else:
        res = max(res, dd)
        left = mid + 1

print(res)
