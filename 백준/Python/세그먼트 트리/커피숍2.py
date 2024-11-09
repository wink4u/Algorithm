import sys
from math import ceil, log2
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

H = ceil(log2(n))
tree_size = 2 ** (H + 1)
tree = [0] * tree_size

def build(left, right, node):
    if left == right:
        tree[node] = arr[left]
        return tree[node]

    mid = (left + right) // 2
    tree[node] = build(left, mid, node * 2) + build(mid + 1, right, node * 2 + 1)
    return tree[node]

def tree_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    return tree_sum(start, mid, node * 2, left, right) + tree_sum(mid + 1, end, node * 2 + 1, left, right)

def update(start, end, node, idx, change):
    if idx < start or idx > end:
        return
    tree[node] += change

    if start != end:
        mid = (start + end) // 2
        update(start, mid, node * 2, idx, change)
        update(mid + 1, end, node * 2 + 1, idx, change)

build(0, n - 1, 1)

for _ in range(m):
    x, y, a, b = map(int, input().split())

    if x > y:
        tmp = y
        y = x
        x = tmp

    print(tree_sum(0, n - 1, 1, x - 1, y - 1))

    a -= 1
    diff = b - arr[a]
    arr[a] = b
    update(0, n - 1, 1, a, diff)