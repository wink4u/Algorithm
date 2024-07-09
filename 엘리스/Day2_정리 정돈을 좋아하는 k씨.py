import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [-1] + list(map(int, input().split()))

for _ in range(m):
    s, e, idx = map(int, input().split())
    tmp = sorted(arr[s:e + 1])
    print(tmp[idx - 1])