import sys
from math import ceil, log2
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

H = ceil(log2(n))
tree_size = 2 ** (H + 1)
min_segment = [0] * tree_size
max_segment = [0] * tree_size

def min_build(left, right, node):
    if left == right:
        min_segment[node] = arr[left]
        return min_segment[node]

    mid = (left + right) // 2
    min_segment[node] = min(min_build(left, mid, node * 2), min_build(mid + 1, right, node * 2 + 1))
    return min_segment[node]


def max_build(left, right, node):
    if left == right:
        max_segment[node] = arr[left]
        return max_segment[node]

    mid = (left + right) // 2
    max_segment[node] = max(max_build(left, mid, node * 2), max_build(mid + 1, right, node * 2 + 1))
    return max_segment[node]

def query_min(start, end, node, left, right):
    if left > end or right < start:
        return 1000000001
    if left <= start and right >= end:
        return min_segment[node]

    mid = (start + end) // 2
    return min(query_min(start, mid, node * 2, left, right), query_min(mid + 1, end, node * 2 + 1, left, right))


def query_max(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return max_segment[node]

    mid = (start + end) // 2
    return max(query_max(start, mid, node * 2, left, right), query_max(mid + 1, end, node * 2 + 1, left, right))


min_build(0, n - 1, 1)
max_build(0, n - 1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    _min, _max = query_min(0, n - 1, 1, a - 1, b - 1), query_max(0, n - 1, 1, a - 1, b - 1)
    print(_min, _max)