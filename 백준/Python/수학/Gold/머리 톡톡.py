import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

stu = defaultdict(int)
p = []

for _ in range(n):
    now = int(input())
    stu[now] += 1
    p.append(now)

v = [0] * 1000001

for i in range(1, 1000001):
    if stu[i]:
        v[i] += stu[i] - 1

        for j in range(2 * i, 1000001, i):
            if stu[j]:
                v[j] += stu[i]

for i in p:
    print(v[i])