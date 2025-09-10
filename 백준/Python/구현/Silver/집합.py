import sys
import heapq
input = sys.stdin.readline

n = int(input())
check = set()
for _ in range(n):
    v = list(input().split())

    if v[0] == 'add':
        check.add(v[1])
    elif v[0] == 'remove':
        if v[1] in check:
            check.remove(v[1])
    elif v[0] == 'check':
        if v[1] in check:
            print(1)
        else:
            print(0)
    elif v[0] == 'toggle':
        if v[1] in check:
            check.remove(v[1])
        else:
            check.add(v[1])
    elif v[0] == 'all':
        check = set(str(i) for i in range(1, 21))
    else:
        check.clear()