import sys
input = sys.stdin.readline

s, k = map(int, input().split())
res = 1

r = [s//k for _ in range(k)]

for i in range(s % k):
    r[i] += 1

for rr in r:
    res *= rr

print(res)