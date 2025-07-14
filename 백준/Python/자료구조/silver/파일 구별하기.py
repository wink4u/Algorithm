import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = []
_max = 0
for _ in range(n):
    tmp = list(input().split())
    l = len(tmp)
    _max = max(_max, l)
    arr.append([l - 1, tmp[:l]])

check = defaultdict(set)

ans = 0
for i in range(1, _max + 1):
    flag = 0
    for k in range(n):
        l_k, l_s = arr[k]
        if l_k < i:
            continue

        c = ''.join(l_s[:i])
        if c in check[i]:
            flag = 1
            break

        check[i].add(c)

    if not flag:
        ans = i
        break

print(ans)