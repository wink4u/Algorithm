import sys
from math import ceil, log2

input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

H = ceil(log2(n))
tree_size = 2 ** (H + 1)
tree = [0] * tree_size

def build(left, right, node):
    if left == right:
        tree[node] = arr[left]
        return tree[node]
    mid = (left + right) // 2
    tree[node] = min(build(left, mid, node * 2), build(mid + 1, right, node * 2 + 1))
    return tree[node]

def check_mid(start, end, node, left, right):
    if left > end or right < start:
        return 1e11

    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    return min(check_mid(start, mid, node * 2, left, right), check_mid(mid + 1, end, node * 2 + 1, left, right))


build(0, n - 1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(check_mid(0, n - 1, 1, a - 1, b - 1))