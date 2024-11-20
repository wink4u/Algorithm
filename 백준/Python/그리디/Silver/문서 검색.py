import sys
from collections import deque
input = sys.stdin.readline

n = input().strip()
m = input().strip()

left, right = 0, len(m)
res = 0
while left < right and right <= len(n):
    s = n[left:right]
    if s == m:
        left += len(m)
        right += len(m)
        res += 1
    else:
        left += 1
        right += 1

print(res)