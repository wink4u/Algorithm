import sys

input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]


# 0, 0 포함된 직사각형 유무 판단

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


def check(rect, c_rect):
    rx1, ry1, rx2, ry2 = rect
    cx1, cy1, cx2, cy2 = c_rect

    if rx1 < cx1 < cx2 < rx2 and ry1 < cy1 < cy2 < ry2:
        return False

    if cx1 < rx1 < rx2 < cx2 and cy1 < ry1 < ry2 < cy2:
        return False

    if rx2 < cx1 or cx2 < rx1 or ry1 > cy2 or cy1 > ry2:
        return False

    return True


def zero(rect):
    rx1, ry1, rx2, ry2 = rect

    if (rx1 <= 0 <= rx2 and 0 in [ry1, ry2]) or (ry1 <= 0 <= ry2 and 0 in [rx1, rx2]):
        return True
    return False


rec = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        if check(rec[i], rec[j]):
            union(i, j)

p_set = set()
flag = 0

for i in range(n):
    idx = find(i)
    p_set.add(idx)

    if not flag and zero(rec[i]):
        flag = 1

res = len(p_set)

print(res - 1 if flag else res)
