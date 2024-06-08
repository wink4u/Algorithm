import sys
input = sys.stdin.readline

N = int(input())

levels = []

for i in range(N):
    levels.append(int(input()))

last = levels[-1]
res = 0
for i in range(N - 2, -1, -1):
    prev = levels[i]
    if last <= prev:
        res += prev - last + 1
        last -= 1
    else:
        last = prev

print(res)