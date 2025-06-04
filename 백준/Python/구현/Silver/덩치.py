import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = []
for x, y in arr:
    now = 1
    for nx, ny in arr:
        if x < nx and y < ny:
            now += 1
    res.append(now)

print(*res)