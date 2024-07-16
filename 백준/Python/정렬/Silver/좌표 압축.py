import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

arr_set = list(set(arr))
arr_set.sort()

res = defaultdict(int)

cnt = 0
for num in arr_set:
    res[num] = cnt
    cnt += 1

ans = []

for num in arr:
    ans.append(res[num])

print(*ans)