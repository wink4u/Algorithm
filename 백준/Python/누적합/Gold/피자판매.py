import sys
from collections import defaultdict
input = sys.stdin.readline

w = int(input())
a, b = map(int, input().split())

ap = [int(input()) for _ in range(a)]
bp = [int(input()) for _ in range(b)]

aa = defaultdict(int)
bb = defaultdict(int)

aa[sum(ap)] += 1
bb[sum(bp)] += 1

for i in range(a):
    now = ap[i]
    for j in range(i + 1, i + a):
        if now > w:
            break
        if i != j:
            aa[now] += 1
            now += ap[j % a]

for i in range(b):
    now = bp[i]
    for j in range(i + 1, i + b):
        if now > w:
            break

        if i != j:
            bb[now] += 1
            now += bp[j % b]

a_key = list(aa.keys())
cnt = 0

if aa[w]:
    cnt += aa[w]

if bb[w]:
    cnt += bb[w]

for i in range(len(a_key)):
    t = w - a_key[i]
    if t > 0 and bb[t]:
        cnt += aa[a_key[i]] * bb[t]

print(cnt)