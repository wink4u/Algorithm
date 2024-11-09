import sys
from math import ceil, log2
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

H = ceil(log2(n))
tree_size = 2 ** (H + 1)
tree = [1] * tree_size
MOD = 1000000007

def build(left, right, node):
    if left == right:
        tree[node] = arr[left]
        return tree[node]

    mid = (left + right) // 2
    tree[node] = build(left, mid, node * 2) * build(mid + 1, right, node * 2 + 1) % MOD
    return tree[node]

def check_tree(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    return check_tree(start, mid, node * 2, left, right) * check_tree(mid + 1, end, node * 2 + 1, left, right) % MOD

def update(start, end, node, idx, change):
    if idx < start or idx > end:
        return

    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, idx, change)
    update(mid + 1, end, node * 2 + 1, idx, change)
    tree[node] = tree[node * 2] * tree[node * 2 + 1] % MOD

build(0, n - 1, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        if arr[b - 1]:
            diff = c / arr[b - 1]
            arr[b - 1] = c
        else:
            diff = c
            arr[b - 1] = c

        update(0, n - 1, 1, b - 1, diff)
    else:
        print(check_tree(0, n - 1, 1, b - 1, c - 1))