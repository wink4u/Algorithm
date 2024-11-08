import sys
from math import ceil, log2
input = sys.stdin.readline

# 입력 받기
n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 세그먼트 트리 초기화
H = ceil(log2(n))
tree_size = 2 ** (H + 1)
segment_tree = [0] * tree_size

# 세그먼트 트리 빌드 함수
def build_segment_tree(left, right, node):
    if left == right:
        segment_tree[node] = arr[left]
        return segment_tree[node]
    mid = (left + right) // 2
    segment_tree[node] = build_segment_tree(left, mid, node * 2) + build_segment_tree(mid + 1, right, node * 2 + 1)
    return segment_tree[node]

# 구간 합 쿼리 함수
def query_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segment_tree[node]
    mid = (start + end) // 2
    return query_sum(start, mid, node * 2, left, right) + query_sum(mid + 1, end, node * 2 + 1, left, right)

# 업데이트 함수
def update(start, end, node, idx, diff):
    if idx < start or idx > end:
        return
    segment_tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node * 2, idx, diff)
        update(mid + 1, end, node * 2 + 1, idx, diff)

# 트리 초기화.3
build_segment_tree(0, n - 1, 1)

# 명령 처리
for _ in range(m + k):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        # 값 변경 명령
        a -= 1  # 1-based index를 0-based로 맞추기
        diff = b - arr[a]
        arr[a] = b
        update(0, n - 1, 1, a, diff)
    elif cmd == 2:
        # 구간 합 명령
        print(query_sum(0, n - 1, 1, a - 1, b - 1))
