import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

_sum = 0
res = 0
check = defaultdict(int)
check[0] = 1

for num in arr:
    _sum += num
    res += check[_sum - k]
    check[_sum] += 1

print(res)