import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

arr = {}
for _ in range(N):
    string = input().strip()
    arr[string] = True

cnt = 0
for _ in range(M):
    now = input().strip()
    if now in arr:
        cnt += 1

print(cnt)
