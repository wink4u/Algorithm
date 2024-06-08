import sys

input = sys.stdin.readline

# 나무의 수 N 집으로 가져가려고 하는 나무의 길이 M
N, M = map(int, input().split())

tree = list(map(int, input().split()))

tree.sort()

L = 0
R = max(tree)


def check(value):
    total = 0
    for i in range(N):
        if tree[i] - value >= 0:
            total += tree[i] - value

    if total >= M:
        return 1
    else:
        return 0


answer = 0
while (L <= R):
    mid = (L + R) // 2

    if (check(mid)):
        L = mid + 1
        answer = mid
    else:
        R = mid - 1

print(answer)

