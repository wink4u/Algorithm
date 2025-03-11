import sys
input = sys.stdin.readline

n, s = map(int, input().split())
picture = dict()
_max = 0

for _ in range(n):
    h, c = map(int, input().split())
    _max = max(_max, h)
    if h in picture:
        picture[h] = max(picture[h], c)
    else:
        picture[h] = c

heights = [0] * (_max + 1)

for k in range(1, len(heights)):
    if k in picture:
        new_cost = picture[k]
        if k-s >= 0:
            new_cost += heights[k-s]
        heights[k] = max(heights[k-1], new_cost)
    else:
        heights[k] = heights[k-1]

print(heights[-1])