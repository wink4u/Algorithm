import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())

parent = list(range(n))
money = list(map(int, input().split()))

def find(a):
    if a == parent[a]:
        return a

    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    pa = find(a)
    pb = find(b)

    if money[pa] < money[pb]:
        parent[pb] = pa
    else:
        parent[pa] = pb

for _ in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

total = 0
check = set()

for i in range(n):
    if find(i) not in check:
        total += money[parent[i]]
        check.add(parent[i])

if total > k:
    print("Oh no")
else:
    print(total)
