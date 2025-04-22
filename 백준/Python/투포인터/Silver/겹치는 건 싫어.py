import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
cnt = 0
check = defaultdict(int)
res = 0

while l <= r and r < n:
    if check[arr[r]] == k:
        check[arr[l]] -= 1
        cnt -= 1
        l += 1
    else:
        check[arr[r]] += 1
        cnt += 1
        r += 1

    res = max(res, cnt)

print(res)